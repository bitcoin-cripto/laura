-- ─────────────────────────────────────────────────────────────────────────────
-- Migración 001 · Unificar ubicacion → lugar
-- Ejecutar en: Supabase Dashboard → SQL Editor
-- ─────────────────────────────────────────────────────────────────────────────

-- 1. Asegurar que existe la columna "lugar" (por si la tabla se creó antes)
ALTER TABLE retiros ADD COLUMN IF NOT EXISTS lugar text;

-- 2. Copiar los datos de "ubicacion" a "lugar" donde "lugar" esté vacío
UPDATE retiros
SET    lugar = ubicacion
WHERE  ubicacion IS NOT NULL
  AND  (lugar IS NULL OR lugar = '');

-- 3. Eliminar la columna "ubicacion"
ALTER TABLE retiros DROP COLUMN IF EXISTS ubicacion;
