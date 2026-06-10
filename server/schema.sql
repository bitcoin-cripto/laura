-- ─────────────────────────────────────────────────────────────────────────────
-- Tabla retiros  ·  Ejecutar en Supabase → SQL Editor
-- ─────────────────────────────────────────────────────────────────────────────

CREATE TABLE IF NOT EXISTS retiros (
  id                uuid          PRIMARY KEY DEFAULT gen_random_uuid(),
  titulo            text          NOT NULL,
  tipo              text          NOT NULL CHECK (tipo IN ('presencial', 'online')),
  fecha_inicio      date          NOT NULL,
  fecha_fin         date,
  precio            numeric(8,2)  NOT NULL,
  lugar             text,                        -- espacio físico o virtual del retiro (único campo de localización)
  descripcion_corta text,
  descripcion_larga text,
  portada_url       text,
  galeria_urls      text[]        DEFAULT '{}',
  creado_en         timestamptz   DEFAULT now()
);

-- Índice para ordenar por fecha en el GET
CREATE INDEX IF NOT EXISTS idx_retiros_fecha ON retiros (fecha_inicio ASC);

-- RLS: habilitar y permitir lectura pública + escritura solo autenticada
ALTER TABLE retiros ENABLE ROW LEVEL SECURITY;

-- Lectura pública (para la web de Laura)
CREATE POLICY "retiros: lectura pública"
  ON retiros FOR SELECT TO anon, authenticated
  USING (true);

-- Escritura solo para usuarios autenticados (tu panel de admin)
CREATE POLICY "retiros: inserción autenticado"
  ON retiros FOR INSERT TO authenticated
  WITH CHECK (true);

CREATE POLICY "retiros: actualización autenticado"
  ON retiros FOR UPDATE TO authenticated
  USING (true) WITH CHECK (true);

CREATE POLICY "retiros: borrado autenticado"
  ON retiros FOR DELETE TO authenticated
  USING (true);
