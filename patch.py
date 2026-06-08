import math, random
random.seed(42)

path = "C:/Users/titurriaga/Downloads/.Claude/Laura/index.html"
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# ── 1. NEW HERO CSS ───────────────────────────────────────────────────────────
hero_css_start = "  /* ---------- HERO ---------- */"
hero_css_end   = "  /* ---------- brush dividers ---------- */"
s = content.find(hero_css_start)
e = content.find(hero_css_end)
assert s != -1 and e != -1, "Hero CSS markers not found"

new_hero_css = """  /* ---------- HERO ---------- */
  .hero{position:relative;min-height:100vh;overflow:hidden;background:var(--sage);}
  .hero-bg{position:absolute;top:0;right:0;width:65%;height:100%;z-index:0;}
  .hero-bg img{width:100%;height:100%;object-fit:cover;object-position:30% top;display:block;}
  .hero-brush-overlay{position:absolute;top:0;left:0;width:100%;height:100%;z-index:1;pointer-events:none;}
  .hero-copy-panel{
    position:relative;z-index:2;
    width:48%;min-height:100vh;
    display:flex;flex-direction:column;justify-content:center;
    padding:120px clamp(24px,5vw,64px) 80px clamp(24px,6vw,90px);
  }
  .hero-copy-panel .eyebrow{color:rgba(253,251,246,.78);margin-bottom:.6em;}
  .hero-name{font-size:clamp(3.2rem,7vw,6rem);color:var(--gold);margin:.1em 0 .4em;text-shadow:0 2px 30px rgba(46,59,53,.3);line-height:1.05;}
  .hero-quote{font-size:clamp(1.25rem,2.2vw,1.8rem);color:var(--white);line-height:1.5;max-width:28ch;margin-bottom:1.8em;}
  .hero-actions{display:flex;align-items:center;gap:26px;flex-wrap:wrap;}
  .hero-actions .btn-earth{background:var(--gold);color:#3c3320;box-shadow:0 14px 30px -14px rgba(0,0,0,.45);}
  .hero-actions .btn-earth:hover{background:#d9bd83;}
  .scroll-cue{position:absolute;bottom:30px;left:25%;transform:translateX(-50%);z-index:4;display:flex;flex-direction:column;align-items:center;gap:8px;color:rgba(253,251,246,.7);font-size:.7rem;letter-spacing:.28em;text-transform:uppercase;}
  .scroll-cue .line{width:1px;height:46px;background:linear-gradient(rgba(253,251,246,.7),transparent);animation:cue 2.4s ease-in-out infinite;}
  @keyframes cue{0%,100%{opacity:.3;transform:scaleY(.7);}50%{opacity:1;transform:scaleY(1);}}

  """

content = content[:s] + new_hero_css + content[e:]

# ── 2. NEW HERO HTML ──────────────────────────────────────────────────────────
hs = content.find('<section class="hero" id="inicio"')
he = content.find('</section>', hs) + len('</section>')
assert hs != -1, "Hero section not found"

new_hero_html = """<section class="hero" id="inicio" data-screen-label="Hero">
  <div class="hero-bg">
    <img src="laura_casa.jpg" alt="Laura Fernandez" />
  </div>
  <svg class="hero-brush-overlay" viewBox="0 0 1440 900" preserveAspectRatio="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
    <path fill="#7aaec4" d="M 0,0 L 624.1,0.0 L 583.3,11.2 L 599.9,22.5 L 583.0,33.8 L 583.1,45.0 L 627.1,56.2 L 606.5,67.5 L 594.3,78.8 L 662.7,90.0 L 612.0,101.2 L 595.6,112.5 L 625.5,123.8 L 618.9,135.0 L 617.8,146.2 L 609.1,157.5 L 603.8,168.8 L 617.7,180.0 L 617.9,191.2 L 639.9,202.5 L 625.5,213.8 L 590.0,225.0 L 605.5,236.2 L 595.3,247.5 L 590.1,258.8 L 600.3,270.0 L 583.0,281.2 L 580.6,292.5 L 605.0,303.8 L 589.0,315.0 L 596.1,326.2 L 605.5,337.5 L 573.8,348.8 L 593.6,360.0 L 571.9,371.2 L 573.0,382.5 L 573.7,393.8 L 565.9,405.0 L 565.5,416.2 L 585.2,427.5 L 563.1,438.8 L 594.0,450.0 L 559.6,461.2 L 581.8,472.5 L 559.1,483.8 L 589.8,495.0 L 590.1,506.2 L 560.7,517.5 L 583.6,528.8 L 572.0,540.0 L 568.8,551.2 L 581.6,562.5 L 597.1,573.8 L 639.1,585.0 L 601.1,596.2 L 595.9,607.5 L 582.4,618.8 L 596.8,630.0 L 629.9,641.2 L 584.0,652.5 L 613.3,663.8 L 647.3,675.0 L 655.4,686.2 L 591.6,697.5 L 651.5,708.8 L 608.7,720.0 L 619.6,731.2 L 598.7,742.5 L 615.3,753.8 L 601.8,765.0 L 612.1,776.2 L 635.1,787.5 L 600.5,798.8 L 595.9,810.0 L 589.5,821.2 L 593.0,832.5 L 639.8,843.8 L 603.6,855.0 L 584.5,866.2 L 596.5,877.5 L 601.2,888.8 L 615.2,900.0 L 0,900 Z"/>
    <path fill="#7aaec4" opacity="0.65" d="M 594,389 C 617,371 652,389 617,406 Z"/>
    <path fill="#7aaec4" opacity="0.42" d="M 592,129 C 608,109 632,129 608,149 Z"/>
    <path fill="#7aaec4" opacity="0.57" d="M 609,388 C 637,373 679,388 637,404 Z"/>
    <path fill="#7aaec4" opacity="0.51" d="M 589,174 C 616,158 657,174 616,190 Z"/>
    <path fill="#7aaec4" opacity="0.61" d="M 582,648 C 602,633 633,648 602,663 Z"/>
    <path fill="#fdfbf6" opacity="0.55" d="M 0,872 C 180,858 380,876 580,864 C 680,858 820,872 960,860 C 1040,854 1140,866 1200,858 L 1200,876 C 1140,882 1040,872 960,878 C 820,890 680,876 580,882 C 380,894 180,878 0,890 Z"/>
    <path fill="#fdfbf6" opacity="0.35" d="M 60,888 C 260,874 460,892 660,880 C 760,874 880,888 1020,878 C 1080,874 1150,884 1260,876 L 1260,893 C 1150,900 1080,892 1020,896 C 880,906 760,893 660,898 C 460,910 260,894 60,906 Z"/>
  </svg>
  <div class="hero-copy-panel">
    <span class="eyebrow" style="font-size:15px;letter-spacing:5px">Conversaciones sobre la naturaleza de la realidad</span>
    <h1 class="hero-name script">Laura Fernandez</h1>
    <p class="hero-quote quote">En la ignorancia soy alguien. En la comprension soy nadie. En el amor soy todo.</p>
    <div class="hero-actions">
      <a href="#retiros" class="btn btn-earth">Retiros</a>
    </div>
  </div>
  <div class="scroll-cue" aria-hidden="true"><div class="line"></div></div>
</section>"""

content = content[:hs] + new_hero_html + content[he:]

# ── 3. MOBILE HERO responsive ─────────────────────────────────────────────────
old_mob = "    /* hero mobile: foto arriba a pantalla completa, texto debajo */"
new_mob = """    /* hero mobile: foto arriba a pantalla completa, texto debajo */
    .hero{display:flex;flex-direction:column;}
    .hero-bg{position:relative;width:100%;height:80vw;flex-shrink:0;}
    .hero-bg img{object-position:center 15%;}
    .hero-brush-overlay{display:none;}
    .hero-copy-panel{
      position:relative;width:100%;min-height:auto;
      padding:36px 28px 60px;
      text-align:center;align-items:center;
      background:var(--sage);
    }
    .hero-name{font-size:clamp(2.8rem,11vw,4.2rem);}
    .hero-quote{font-size:1.2rem;text-align:center;max-width:100%;}
    .hero-actions{justify-content:center;}
    .scroll-cue{display:none;}"""

if old_mob in content:
    # Replace from old_mob to end of that block
    ms = content.find(old_mob)
    # find next media block or end of this block
    me = content.find("\n  }", ms) + 4
    content = content[:ms] + new_mob + content[me:]
    print("Mobile block replaced")
else:
    # Inject into the 768px media query
    m768 = content.find("  @media(max-width:768px){")
    closing = content.find("\n  }", m768)
    content = content[:closing] + "\n" + new_mob + content[closing:]
    print("Mobile block injected into 768px query")

# ── 4. MOVE ¿Conversamos? section BEFORE reserva ─────────────────────────────
CONV_MARKER  = "<!-- ===================== ¿CONVERSAMOS? ===================== -->"
RESERVA_MARKER = "<!-- ===================== RESERVA Y PAGO ===================== -->"
ONLINE_END_MARKER = "<!-- brush: cream-warm -> sage-wash -->"

conv_section_start = content.find(CONV_MARKER)
reserva_pos = content.find(RESERVA_MARKER)

if conv_section_start == -1 or reserva_pos == -1:
    print("Section markers not found — skipping reorder")
else:
    # Find the brush divider right before conversamos
    brush_before_conv = content.rfind("<!-- brush:", 0, conv_section_start)
    # The conversamos block ends at the RESERVA marker (current position)
    conv_block = content[brush_before_conv:reserva_pos]
    content_no_conv = content[:brush_before_conv] + content[reserva_pos:]

    # Now in content_no_conv, find where to insert: before reserva (which is now right there)
    # We want to insert BEFORE the brush that leads to reserva
    # The online section ends with a brush, then reserva follows — insert AFTER that brush
    reserva_pos2 = content_no_conv.find(RESERVA_MARKER)
    brush_before_reserva = content_no_conv.rfind("<!-- brush:", 0, reserva_pos2)

    content = content_no_conv[:brush_before_reserva] + conv_block + content_no_conv[brush_before_reserva:]
    print("Section reordered OK")

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
print("File written OK. Length:", len(content))
