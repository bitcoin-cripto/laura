// ─────────────────────────────────────────────────────────────────────────────
// server.js  ·  Backend Laura Fernández No Dualidad
// Stack: Node.js + Express + Multer (memoria) + Supabase JS v2
// ─────────────────────────────────────────────────────────────────────────────

'use strict';

require('dotenv').config();

const express   = require('express');
const multer    = require('multer');
const { createClient } = require('@supabase/supabase-js');
const path      = require('path');

// ── Validación de variables de entorno ───────────────────────────────────────
const { SUPABASE_URL, SUPABASE_KEY, PORT = 4000 } = process.env;
if (!SUPABASE_URL || !SUPABASE_KEY) {
  console.error('❌  Faltan SUPABASE_URL o SUPABASE_KEY en el archivo .env');
  process.exit(1);
}

// ── Clientes ─────────────────────────────────────────────────────────────────
const app      = express();
const supabase = createClient(SUPABASE_URL, SUPABASE_KEY);

// ── Multer: almacenamiento en memoria (no toca el disco) ──────────────────────
// Límite: portada 5 MB · galería 8 MB por imagen · máx. 10 imágenes de galería
const upload = multer({
  storage: multer.memoryStorage(),
  limits: { fileSize: 8 * 1024 * 1024 },
  fileFilter: (_req, file, cb) => {
    const allowed = /^image\/(jpeg|png|webp|gif)$/;
    allowed.test(file.mimetype)
      ? cb(null, true)
      : cb(new Error(`Tipo de archivo no permitido: ${file.mimetype}`));
  },
});

const uploadFields = upload.fields([
  { name: 'portada',  maxCount: 1  },
  { name: 'galeria',  maxCount: 10 },
]);

// ── Middlewares globales ──────────────────────────────────────────────────────
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// CORS permisivo para desarrollo local
app.use((_req, res, next) => {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, DELETE, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type, Authorization');
  next();
});

// ── Helpers ───────────────────────────────────────────────────────────────────

/**
 * Sube un archivo (Buffer) al bucket "imgs" de Supabase Storage.
 * Devuelve la URL pública permanente del objeto.
 *
 * @param {Buffer} buffer   - contenido del archivo
 * @param {string} mimetype - p.ej. "image/jpeg"
 * @param {string} folder   - subcarpeta dentro del bucket, p.ej. "retiros/portadas"
 * @param {string} originalname
 * @returns {Promise<string>} URL pública
 */
async function subirImagen(buffer, mimetype, folder, originalname) {
  const ext      = path.extname(originalname) || '.jpg';
  const filename = `${folder}/${Date.now()}-${Math.random().toString(36).slice(2)}${ext}`;

  const { error } = await supabase.storage
    .from('imgs')
    .upload(filename, buffer, {
      contentType:  mimetype,
      cacheControl: '3600',
      upsert:       false,
    });

  if (error) throw new Error(`Storage upload: ${error.message}`);

  const { data } = supabase.storage.from('imgs').getPublicUrl(filename);
  return data.publicUrl;
}

// ─────────────────────────────────────────────────────────────────────────────
// RUTAS
// ─────────────────────────────────────────────────────────────────────────────

// ── GET /api/retiros ──────────────────────────────────────────────────────────
// Devuelve todos los retiros ordenados por fecha_inicio (ascendente).
// Los futuros aparecen primero; los pasados al final.
app.get('/api/retiros', async (_req, res) => {
  const { data, error } = await supabase
    .from('retiros')
    .select('*')
    .order('fecha_inicio', { ascending: true });

  if (error) return res.status(500).json({ ok: false, error: error.message });
  return res.json({ ok: true, data });
});

// ── POST /api/retiros ─────────────────────────────────────────────────────────
// Crea un nuevo retiro con portada + galería opcional.
//
// Form-data esperado:
//   titulo            string   requerido
//   tipo              "presencial" | "online"
//   fecha_inicio      string   ISO date  (YYYY-MM-DD)
//   fecha_fin         string   ISO date  (YYYY-MM-DD)  opcional
//   precio            number
//   ubicacion         string   (para presenciales)
//   descripcion_corta string   (máx. ~160 chars recomendado)
//   descripcion_larga string
//   portada           File     imagen principal del retiro
//   galeria           File[]   hasta 10 imágenes adicionales (opcional)
app.post('/api/retiros', uploadFields, async (req, res) => {
  try {
    const {
      titulo,
      tipo,
      fecha_inicio,
      fecha_fin,
      precio,
      lugar,
      ubicacion,
      descripcion_corta,
      descripcion_larga,
    } = req.body;

    // ── Validación básica ─────────────────────────────────────────────────
    const errores = [];
    if (!titulo)        errores.push('titulo es obligatorio');
    if (!tipo)          errores.push('tipo es obligatorio (presencial | online)');
    if (!fecha_inicio)  errores.push('fecha_inicio es obligatoria');
    if (!precio)        errores.push('precio es obligatorio');
    if (errores.length) return res.status(400).json({ ok: false, errores });

    // ── Subida de portada ─────────────────────────────────────────────────
    let portada_url = null;
    if (req.files?.portada?.[0]) {
      const f = req.files.portada[0];
      portada_url = await subirImagen(f.buffer, f.mimetype, 'retiros/portadas', f.originalname);
    }

    // ── Subida de galería ─────────────────────────────────────────────────
    let galeria_urls = [];
    if (req.files?.galeria?.length) {
      galeria_urls = await Promise.all(
        req.files.galeria.map(f =>
          subirImagen(f.buffer, f.mimetype, 'retiros/galeria', f.originalname)
        )
      );
    }

    // ── Inserción en la tabla retiros ─────────────────────────────────────
    const { data, error } = await supabase
      .from('retiros')
      .insert([{
        titulo,
        tipo,
        fecha_inicio,
        fecha_fin:         fecha_fin         || null,
        precio:            parseFloat(precio),
        lugar:             lugar             || null,
        ubicacion:         ubicacion         || null,
        descripcion_corta: descripcion_corta || null,
        descripcion_larga: descripcion_larga || null,
        portada_url,
        galeria_urls,       // array de texto en Postgres (tipo text[])
      }])
      .select()
      .single();

    if (error) return res.status(500).json({ ok: false, error: error.message });

    return res.status(201).json({ ok: true, data });

  } catch (err) {
    console.error('POST /api/retiros:', err);
    return res.status(500).json({ ok: false, error: err.message });
  }
});

// ── DELETE /api/retiros/:id ───────────────────────────────────────────────────
// Borra el retiro y sus imágenes del Storage.
app.delete('/api/retiros/:id', async (req, res) => {
  const { id } = req.params;

  try {
    // 1. Recuperar la fila para obtener las URLs de imágenes
    const { data: retiro, error: fetchErr } = await supabase
      .from('retiros')
      .select('portada_url, galeria_urls')
      .eq('id', id)
      .single();

    if (fetchErr) return res.status(404).json({ ok: false, error: 'Retiro no encontrado' });

    // 2. Construir la lista de paths a borrar del Storage
    //    Las URLs públicas tienen el formato:
    //    https://<project>.supabase.co/storage/v1/object/public/imgs/<path>
    const toDelete = [];
    const extractPath = url => {
      if (!url) return null;
      const marker = '/object/public/imgs/';
      const idx    = url.indexOf(marker);
      return idx !== -1 ? url.slice(idx + marker.length) : null;
    };

    if (retiro.portada_url) {
      const p = extractPath(retiro.portada_url);
      if (p) toDelete.push(p);
    }
    if (Array.isArray(retiro.galeria_urls)) {
      retiro.galeria_urls.forEach(url => {
        const p = extractPath(url);
        if (p) toDelete.push(p);
      });
    }

    // 3. Borrar imágenes del bucket (ignoramos errores individuales)
    if (toDelete.length) {
      const { error: storageErr } = await supabase.storage
        .from('imgs')
        .remove(toDelete);
      if (storageErr) {
        console.warn('Aviso: no se pudieron borrar algunas imágenes del Storage:', storageErr.message);
      }
    }

    // 4. Borrar la fila de la base de datos
    const { error: deleteErr } = await supabase
      .from('retiros')
      .delete()
      .eq('id', id);

    if (deleteErr) return res.status(500).json({ ok: false, error: deleteErr.message });

    return res.json({ ok: true, message: `Retiro ${id} eliminado correctamente` });

  } catch (err) {
    console.error('DELETE /api/retiros/:id:', err);
    return res.status(500).json({ ok: false, error: err.message });
  }
});

// ── Ruta de salud ─────────────────────────────────────────────────────────────
app.get('/api/health', (_req, res) => {
  res.json({ ok: true, ts: new Date().toISOString() });
});

// ── Arranque ──────────────────────────────────────────────────────────────────
app.listen(PORT, () => {
  console.log(`✅  Servidor escuchando en http://localhost:${PORT}`);
  console.log(`    GET    http://localhost:${PORT}/api/retiros`);
  console.log(`    POST   http://localhost:${PORT}/api/retiros`);
  console.log(`    DELETE http://localhost:${PORT}/api/retiros/:id`);
});
