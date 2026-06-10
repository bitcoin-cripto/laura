# -*- coding: utf-8 -*-
NEW_MAIN = '''\
<main class="max-w-7xl mx-auto px-4 sm:px-6 py-8">

  <!-- VISTA A: TABLA DE GESTIÓN -->
  <section id="vista-tabla">
    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4 mb-6">
      <div>
        <p class="text-xs font-semibold tracking-widest text-earth uppercase mb-1">Panel de administración</p>
        <h1 class="font-serif text-4xl text-sage-dark font-light">Retiros publicados</h1>
      </div>
      <div class="flex items-center gap-3">
        <button onclick="cargarRetiros()"
                class="flex items-center gap-1.5 text-xs font-semibold text-sage-dark
                       hover:text-earth transition-colors px-3 py-2 rounded-lg
                       border border-gray-200 hover:border-earth bg-white">
          <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                  d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"/>
          </svg>
          Actualizar
        </button>
        <button onclick="mostrarFormulario()"
                class="flex items-center gap-2 bg-sage-dark hover:bg-sage text-white
                       font-semibold text-sm px-5 py-2.5 rounded-xl transition-colors shadow-sm">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"/>
          </svg>
          Nuevo retiro
        </button>
      </div>
    </div>

    <div class="bg-white rounded-2xl shadow-sm border border-gray-100 overflow-hidden">
      <div id="tabla-estado" class="flex flex-col items-center justify-center py-16 text-gray-400 gap-3">
        <svg class="w-10 h-10 text-gray-200" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"
                d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"/>
        </svg>
        <p class="text-sm">Cargando retiros…</p>
      </div>
      <div id="tabla-wrap" class="hidden overflow-x-auto">
        <table class="w-full text-sm">
          <thead class="bg-gray-50 border-b border-gray-100">
            <tr>
              <th class="text-left px-5 py-3.5 text-xs font-semibold tracking-widest text-gray-400 uppercase">Portada</th>
              <th class="text-left px-5 py-3.5 text-xs font-semibold tracking-widest text-gray-400 uppercase">Título</th>
              <th class="text-left px-4 py-3.5 text-xs font-semibold tracking-widest text-gray-400 uppercase">Tipo</th>
              <th class="text-left px-4 py-3.5 text-xs font-semibold tracking-widest text-gray-400 uppercase">Fecha inicio</th>
              <th class="text-left px-4 py-3.5 text-xs font-semibold tracking-widest text-gray-400 uppercase">Precio</th>
              <th class="text-left px-4 py-3.5 text-xs font-semibold tracking-widest text-gray-400 uppercase">Lugar</th>
              <th class="px-4 py-3.5"></th>
            </tr>
          </thead>
          <tbody id="tabla-retiros" class="divide-y divide-gray-50"></tbody>
        </table>
      </div>
    </div>
  </section>

  <!-- VISTA B: FORMULARIO NUEVO / EDITAR -->
  <section id="vista-formulario" class="hidden">

    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4 mb-6">
      <div class="flex items-center gap-4">
        <button type="button" onclick="mostrarTabla()"
                class="flex items-center gap-1 text-sm text-gray-400 hover:text-ink transition-colors">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"/>
          </svg>
          Volver
        </button>
        <div class="h-5 w-px bg-gray-200"></div>
        <div>
          <p class="text-xs font-semibold tracking-widest text-earth uppercase">Panel de administración</p>
          <h1 id="form-titulo-label" class="font-serif text-3xl text-sage-dark font-light">Nuevo retiro</h1>
        </div>
      </div>
      <div class="flex items-center gap-3">
        <button type="button" onclick="mostrarTabla()"
                class="px-5 py-2.5 rounded-xl border border-gray-200 text-sm font-semibold
                       text-gray-500 hover:bg-gray-50 transition">
          Cancelar
        </button>
        <button type="submit" form="form-retiro" id="btn-submit"
                class="flex items-center gap-2 bg-sage-dark hover:bg-sage text-white
                       font-semibold text-sm px-7 py-2.5 rounded-xl transition-colors shadow-sm">
          <svg id="submit-spinner" class="hidden animate-spin w-4 h-4" fill="none" viewBox="0 0 24 24">
            <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"/>
            <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8v8z"/>
          </svg>
          <span id="submit-text">Publicar retiro</span>
        </button>
      </div>
    </div>

    <form id="form-retiro" novalidate autocomplete="off">
      <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">

        <!-- Columna izquierda 2/3 -->
        <div class="lg:col-span-2 space-y-6">

          <div class="bg-white rounded-2xl shadow-sm border border-gray-100 p-6">
            <label class="block text-xs font-semibold tracking-widest text-gray-500 uppercase mb-2">
              Título <span class="text-red-400">*</span>
            </label>
            <input id="titulo" name="titulo" type="text" required
                   placeholder="Ej: El silencio es lo que eres"
                   class="w-full rounded-lg border border-gray-200 px-4 py-3 text-base
                          focus:outline-none focus:ring-2 focus:ring-sage/40 focus:border-sage
                          placeholder-gray-300 transition"/>
          </div>

          <div class="bg-white rounded-2xl shadow-sm border border-gray-100 p-6">
            <label class="block text-xs font-semibold tracking-widest text-gray-500 uppercase mb-1">
              Descripción corta
              <span class="ml-2 text-gray-400 normal-case font-normal tracking-normal">(tarjeta del retiro · ~160 caracteres)</span>
            </label>
            <textarea id="descripcion_corta" name="descripcion_corta" rows="3"
                      placeholder="Una frase breve que invite a explorar…"
                      class="w-full rounded-lg border border-gray-200 px-4 py-2.5 text-sm mt-2
                             focus:outline-none focus:ring-2 focus:ring-sage/40 focus:border-sage
                             placeholder-gray-300 resize-none transition"></textarea>
          </div>

          <div class="bg-white rounded-2xl shadow-sm border border-gray-100 p-6">
            <div class="flex items-center justify-between mb-3">
              <label class="block text-xs font-semibold tracking-widest text-gray-500 uppercase">
                Descripción larga
                <span class="ml-2 text-gray-400 normal-case font-normal tracking-normal">(editor enriquecido)</span>
              </label>
              <div class="relative" id="emoji-anchor">
                <button type="button" id="btn-emoji"
                        class="flex items-center gap-1.5 text-xs text-gray-400 hover:text-earth
                               transition-colors px-3 py-1.5 rounded-lg hover:bg-gray-50 border border-gray-200">
                  \U0001f60a Emoji
                </button>
                <div id="emoji-picker-wrapper"></div>
              </div>
            </div>
            <div id="quill-editor"></div>
            <input type="hidden" id="descripcion_larga" name="descripcion_larga"/>
          </div>

          <div class="bg-white rounded-2xl shadow-sm border border-gray-100 p-6">
            <label class="block text-xs font-semibold tracking-widest text-gray-500 uppercase mb-3">
              Galería de imágenes
            </label>
            <label for="galeria"
                   class="dropzone flex flex-col items-center justify-center gap-2
                          border-2 border-dashed border-gray-200 rounded-xl p-6 cursor-pointer
                          hover:border-sage hover:bg-blue-50/30 transition group">
              <svg class="w-8 h-8 text-gray-300 group-hover:text-sage transition" fill="none"
                   stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"
                      d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"/>
              </svg>
              <span class="text-sm text-gray-400 group-hover:text-sage transition" id="galeria-label">Selecciona hasta 10 imágenes</span>
              <span class="text-xs text-gray-300">Selección múltiple permitida</span>
              <input id="galeria" name="galeria" type="file" accept="image/*" multiple class="sr-only"/>
            </label>
            <div id="galeria-preview" class="hidden grid grid-cols-5 gap-2 mt-3"></div>

            <div class="mt-6 space-y-3">
              <p class="text-xs text-gray-400 font-medium">¿No tienes las imágenes? Búscalas o pega una URL:</p>
              <div class="flex gap-2">
                <input id="unsplash-galeria-query" type="text" placeholder="Ej: retiro de meditación, naturaleza…"
                       class="flex-1 rounded-lg border border-gray-200 px-3 py-2 text-sm
                              focus:outline-none focus:ring-2 focus:ring-sage/40 focus:border-sage
                              placeholder-gray-300 transition"/>
                <button type="button" id="btn-unsplash-galeria-search"
                        class="flex items-center gap-1.5 bg-sage-dark hover:bg-sage text-white
                               text-xs font-semibold px-4 py-2 rounded-lg transition-colors whitespace-nowrap">
                  <svg id="unsplash-galeria-spinner" class="hidden animate-spin w-3.5 h-3.5" fill="none" viewBox="0 0 24 24">
                    <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"/>
                    <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8v8z"/>
                  </svg>
                  <svg id="unsplash-galeria-icon" class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-4.35-4.35M17 11A6 6 0 105 11a6 6 0 0012 0z"/>
                  </svg>
                  Buscar
                </button>
              </div>
              <div id="unsplash-galeria-results" class="hidden space-y-2">
                <div id="unsplash-galeria-grid" class="grid grid-cols-4 gap-2 max-h-64 overflow-y-auto pr-1"></div>
                <div class="flex items-center justify-between bg-sage/10 border border-sage/20 rounded-lg px-3 py-2">
                  <span id="galeria-sel-count" class="text-xs font-semibold text-sage-dark">0 imágenes seleccionadas (máx. 10)</span>
                  <button type="button" id="btn-galeria-confirmar" disabled
                          class="flex items-center gap-1.5 bg-sage-dark text-white text-xs font-semibold
                                 px-4 py-1.5 rounded-lg transition-colors disabled:opacity-40
                                 disabled:cursor-not-allowed hover:bg-sage">
                    <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/>
                    </svg>
                    <span id="btn-galeria-confirmar-txt">Añadir seleccionadas</span>
                  </button>
                </div>
                <p class="text-xs text-gray-300 text-right">Imágenes de Unsplash</p>
              </div>
              <div class="flex gap-2">
                <input id="galeria-url-input" type="url" placeholder="O pega aquí la URL de una imagen…"
                       class="flex-1 rounded-lg border border-gray-200 px-3 py-2 text-sm
                              focus:outline-none focus:ring-2 focus:ring-sage/40 focus:border-sage
                              placeholder-gray-300 transition"/>
                <button type="button" id="btn-galeria-url"
                        class="flex items-center gap-1.5 bg-earth hover:bg-earth/80 text-white
                               text-xs font-semibold px-4 py-2 rounded-lg transition-colors whitespace-nowrap">
                  <svg id="galeria-url-spinner" class="hidden animate-spin w-3.5 h-3.5" fill="none" viewBox="0 0 24 24">
                    <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"/>
                    <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8v8z"/>
                  </svg>
                  Añadir URL
                </button>
              </div>
            </div>
          </div>

        </div><!-- /col-span-2 -->

        <!-- Columna derecha 1/3 -->
        <div class="space-y-6">

          <div class="bg-white rounded-2xl shadow-sm border border-gray-100 p-6">
            <h3 class="text-xs font-semibold tracking-widest text-gray-500 uppercase border-b border-gray-100 pb-3 mb-5">
              Datos del retiro
            </h3>
            <div class="space-y-5">
              <div class="space-y-1.5">
                <label class="block text-xs font-semibold tracking-widest text-gray-500 uppercase">
                  Tipo <span class="text-red-400">*</span>
                </label>
                <select id="tipo" name="tipo" required
                        class="w-full rounded-lg border border-gray-200 px-4 py-2.5 text-sm
                               focus:outline-none focus:ring-2 focus:ring-sage/40 focus:border-sage
                               bg-white transition cursor-pointer">
                  <option value="">&#8212; Selecciona &#8212;</option>
                  <option value="presencial">Presencial</option>
                  <option value="online">Online</option>
                </select>
              </div>
              <div class="space-y-1.5">
                <label class="block text-xs font-semibold tracking-widest text-gray-500 uppercase">Lugar</label>
                <input id="lugar" name="lugar" type="text"
                       placeholder="Sierra de Gredos · Online vía Zoom"
                       class="w-full rounded-lg border border-gray-200 px-4 py-2.5 text-sm
                              focus:outline-none focus:ring-2 focus:ring-sage/40 focus:border-sage
                              placeholder-gray-300 transition"/>
              </div>
              <div class="space-y-1.5">
                <label class="block text-xs font-semibold tracking-widest text-gray-500 uppercase">
                  Fecha inicio <span class="text-red-400">*</span>
                </label>
                <input id="fecha_inicio" name="fecha_inicio" type="date" required
                       class="w-full rounded-lg border border-gray-200 px-4 py-2.5 text-sm
                              focus:outline-none focus:ring-2 focus:ring-sage/40 focus:border-sage transition"/>
              </div>
              <div class="space-y-1.5">
                <label class="block text-xs font-semibold tracking-widest text-gray-500 uppercase">Fecha fin</label>
                <input id="fecha_fin" name="fecha_fin" type="date"
                       class="w-full rounded-lg border border-gray-200 px-4 py-2.5 text-sm
                              focus:outline-none focus:ring-2 focus:ring-sage/40 focus:border-sage transition"/>
              </div>
              <div class="space-y-1.5">
                <label class="block text-xs font-semibold tracking-widest text-gray-500 uppercase">
                  Precio (€) <span class="text-red-400">*</span>
                </label>
                <input id="precio" name="precio" type="number" min="0" step="0.01" required
                       placeholder="0.00"
                       class="w-full rounded-lg border border-gray-200 px-4 py-2.5 text-sm
                              focus:outline-none focus:ring-2 focus:ring-sage/40 focus:border-sage
                              placeholder-gray-300 transition"/>
              </div>
            </div>
          </div>

          <div class="bg-white rounded-2xl shadow-sm border border-gray-100 p-6">
            <h3 class="text-xs font-semibold tracking-widest text-gray-500 uppercase border-b border-gray-100 pb-3 mb-5">
              Imagen de portada
            </h3>
            <label for="portada"
                   class="dropzone flex flex-col items-center justify-center gap-2
                          border-2 border-dashed border-gray-200 rounded-xl p-5 cursor-pointer
                          hover:border-sage hover:bg-blue-50/30 transition group">
              <svg class="w-7 h-7 text-gray-300 group-hover:text-sage transition" fill="none"
                   stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"
                      d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"/>
              </svg>
              <span class="text-sm text-gray-400 group-hover:text-sage transition text-center" id="portada-label">
                Arrastra o haz clic
              </span>
              <span class="text-xs text-gray-300">JPG, PNG, WEBP · máx. 5 MB</span>
              <input id="portada" name="portada" type="file" accept="image/*" class="sr-only"/>
            </label>
            <div id="portada-preview" class="hidden mt-3 rounded-lg overflow-hidden border border-gray-100">
              <img id="portada-img" src="" alt="Preview portada" class="w-full h-44 object-cover"/>
            </div>

            <div class="mt-6 space-y-3">
              <p class="text-xs text-gray-400 font-medium">¿No tienes la imagen? Búscala o pega una URL:</p>
              <div class="flex gap-2">
                <input id="unsplash-query" type="text" placeholder="Ej: meditación, naturaleza…"
                       class="flex-1 min-w-0 rounded-lg border border-gray-200 px-3 py-2 text-sm
                              focus:outline-none focus:ring-2 focus:ring-sage/40 focus:border-sage
                              placeholder-gray-300 transition"/>
                <button type="button" id="btn-unsplash-search"
                        class="flex items-center gap-1 bg-sage-dark hover:bg-sage text-white
                               text-xs font-semibold px-3 py-2 rounded-lg transition-colors whitespace-nowrap">
                  <svg id="unsplash-spinner" class="hidden animate-spin w-3.5 h-3.5" fill="none" viewBox="0 0 24 24">
                    <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"/>
                    <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8v8z"/>
                  </svg>
                  <svg id="unsplash-icon" class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                          d="M21 21l-4.35-4.35M17 11A6 6 0 105 11a6 6 0 0012 0z"/>
                  </svg>
                  Buscar
                </button>
              </div>
              <div id="unsplash-results" class="hidden">
                <div id="unsplash-grid" class="grid grid-cols-2 gap-2 max-h-52 overflow-y-auto pr-1"></div>
                <p class="text-xs text-gray-300 mt-1.5 text-right">Imágenes de Unsplash</p>
              </div>
              <div class="flex gap-2">
                <input id="portada-url-input" type="url" placeholder="O pega la URL de una imagen…"
                       class="flex-1 min-w-0 rounded-lg border border-gray-200 px-3 py-2 text-sm
                              focus:outline-none focus:ring-2 focus:ring-sage/40 focus:border-sage
                              placeholder-gray-300 transition"/>
                <button type="button" id="btn-portada-url"
                        class="flex items-center gap-1 bg-earth hover:bg-earth/80 text-white
                               text-xs font-semibold px-3 py-2 rounded-lg transition-colors whitespace-nowrap">
                  <svg id="portada-url-spinner" class="hidden animate-spin w-3.5 h-3.5" fill="none" viewBox="0 0 24 24">
                    <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"/>
                    <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8v8z"/>
                  </svg>
                  Añadir URL
                </button>
              </div>
            </div>
          </div>

          <p class="text-xs text-gray-400 px-1">Los campos con <span class="text-red-400">*</span> son obligatorios.</p>

        </div><!-- /col-span-1 -->

      </div><!-- /grid -->
    </form>
  </section>

</main>'''

with open('C:/Users/titurriaga/Downloads/.Claude/Laura/admin/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

start = content.find('<main ')
end   = content.find('</main>') + len('</main>')

new_content = content[:start] + NEW_MAIN + content[end:]

with open('C:/Users/titurriaga/Downloads/.Claude/Laura/admin/index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"OK. Replaced {end-start} chars with {len(NEW_MAIN)} chars. New total: {len(new_content)}")
