"""Fix the collapsed body HTML in index.html and inject Telha Clarke section bars + marquees."""

NEW_BODY = '''<body>

  <!-- Page Transition Curtain -->
  <div id="page-curtain"
    style="position:fixed;inset:0;z-index:10000;background:#111;pointer-events:none;transform-origin:bottom;transform:scaleY(0);">
  </div>

  <!-- Custom Cursor -->
  <div id="cursor"></div>
  <div id="cursor-ring"></div>

  <!-- NAV -->
  <nav id="main-nav">
    <a href="#hero" class="nav-logo">Camilo Novillo</a>
    <ul class="nav-links">
      <li><a href="#proyectos">Trabajo</a></li>
      <li><a href="#proceso">Proceso</a></li>
      <li><a href="#estudio">Estudio</a></li>
    </ul>
    <a href="#contacto" class="nav-contact-btn">Contacto</a>
  </nav>

  <!-- HERO -->
  <section id="hero">
    <div class="hero-bg">
      <div class="hero-bg-grid"></div>
      <div class="hero-glow"></div>
      <div class="hero-dot-accent"></div>
    </div>
    <div class="hero-year">Buenos Aires · ARG</div>
    <div class="hero-content">
      <p class="hero-label">Portafolio · 2024</p>
      <h1 class="hero-title">
        <span class="line"><span>Camilo</span></span>
        <span class="line"><span>Novillo</span></span>
        <span class="line accent-line"><span>Diseñador.</span></span>
      </h1>
      <div class="hero-meta">
        <p class="hero-description">
          Diseño visual que conecta marcas con personas. Especializado en branding, publicidad digital y sistemas de diseño.
        </p>
        <a href="#proyectos" class="hero-scroll">
          <span class="scroll-line"></span>
          Ver trabajo
        </a>
      </div>
    </div>
  </section>

  <!-- TICKER -->
  <div class="ticker" aria-hidden="true">
    <div class="ticker-track">
      <span>Brand Identity</span><span class="sep">·</span>
      <span>Social Media Ads</span><span class="sep">·</span>
      <span>Google Ads</span><span class="sep">·</span>
      <span>Meta Ads</span><span class="sep">·</span>
      <span>Diseño Web</span><span class="sep">·</span>
      <span>Sistemas de Diseño</span><span class="sep">·</span>
      <span>Manual de Marca</span><span class="sep">·</span>
      <span>Storyboarding</span><span class="sep">·</span>
      <!-- duplicate for loop -->
      <span>Brand Identity</span><span class="sep">·</span>
      <span>Social Media Ads</span><span class="sep">·</span>
      <span>Google Ads</span><span class="sep">·</span>
      <span>Meta Ads</span><span class="sep">·</span>
      <span>Diseño Web</span><span class="sep">·</span>
      <span>Sistemas de Diseño</span><span class="sep">·</span>
      <span>Manual de Marca</span><span class="sep">·</span>
      <span>Storyboarding</span><span class="sep">·</span>
    </div>
  </div>

  <!-- SECTION BAR: 01 SOBRE MÍ -->
  <div class="section-bar" id="bar-about">
    <span class="section-bar-num">01</span>
    <div class="section-bar-line"></div>
    <span class="section-bar-label">Sobre mí</span>
  </div>

  <!-- ABOUT -->
  <section id="about">
    <div class="about-text reveal">
      <p class="section-label clip-reveal">Sobre mí</p>
      <h2 class="section-title clip-reveal delay-1">Impulsado por las ideas. Definido por el detalle.</h2>
      <p class="section-body">
        Soy diseñador gráfico con experiencia en la creación de sistemas visuales que comunican con claridad y estilo.
        Mi trabajo abarca desde la construcción de marcas desde cero hasta el diseño de campañas publicitarias en
        múltiples formatos y plataformas.
      </p>
      <p class="section-body">
        Trabajo con empresas y agencias para traducir sus objetivos de negocio en piezas visuales que generan impacto
        real — en pantalla y en la mente de las personas.
      </p>
      <div class="about-stats">
        <div class="reveal" style="transition-delay:0.1s">
          <div class="stat-num">5<span>+</span></div>
          <div class="stat-label">Años de experiencia</div>
        </div>
        <div class="reveal" style="transition-delay:0.2s">
          <div class="stat-num">30<span>+</span></div>
          <div class="stat-label">Proyectos entregados</div>
        </div>
        <div class="reveal" style="transition-delay:0.3s">
          <div class="stat-num">3<span>+</span></div>
          <div class="stat-label">Clientes recurrentes</div>
        </div>
        <div class="reveal" style="transition-delay:0.4s">
          <div class="stat-num">∞</div>
          <div class="stat-label">Atención al detalle</div>
        </div>
      </div>
    </div>
    <div class="about-visual reveal" style="transition-delay:0.2s">
      <div class="about-visual-inner"></div>
      <div class="about-accent-line"></div>
      <div class="about-dot"></div>
      <div class="about-visual-text">
        <h3>Camilo Novillo</h3>
        <p>Diseñador Gráfico · Buenos Aires, ARG</p>
      </div>
    </div>
  </section>

  <!-- SECTION BAR: 02 PROYECTOS -->
  <div class="section-bar" id="bar-proyectos">
    <span class="section-bar-num">02</span>
    <div class="section-bar-line"></div>
    <span class="section-bar-label">Trabajo</span>
  </div>

  <!-- PROYECTOS -->
  <section id="proyectos">
    <div class="projects-header reveal">
      <div>
        <p class="section-label clip-reveal">Trabajo seleccionado</p>
        <h2 class="section-title clip-reveal delay-1">Proyectos</h2>
      </div>
      <span class="projects-count">05 proyectos</span>
    </div>
    <div class="projects-grid">

      <a class="project-card card-1 reveal" href="project.html?id=1">
        <div class="card-bg"></div>
        <div class="card-num">01</div>
        <div class="card-tag">Branding</div>
        <div class="card-content">
          <div class="card-category">Identidad Visual · DealerNET</div>
          <h3 class="card-title">Guía de Diseño Web</h3>
          <p class="card-desc">Sistema completo de marca y estándares de diseño web. 91 páginas de especificaciones visuales.</p>
          <div class="card-cta"><span class="card-cta-line"></span> Ver proyecto</div>
        </div>
      </a>

      <a class="project-card card-2 reveal" style="transition-delay:0.1s" href="project.html?id=2">
        <div class="card-bg"></div>
        <div class="card-num">02</div>
        <div class="card-tag">Documentación</div>
        <div class="card-content">
          <div class="card-category">Editorial · DealerNET</div>
          <h3 class="card-title">Manual de Cliente</h3>
          <p class="card-desc">Documentación visual y funcional diseñada para guiar a los usuarios de la plataforma.</p>
          <div class="card-cta"><span class="card-cta-line"></span> Ver proyecto</div>
        </div>
      </a>

      <a class="project-card card-3 reveal" style="transition-delay:0.2s" href="project.html?id=3">
        <div class="card-bg"></div>
        <div class="card-num">03</div>
        <div class="card-tag">Social Media</div>
        <div class="card-content">
          <div class="card-category">Publicidad Digital · DealerNET</div>
          <h3 class="card-title">Anuncios para Redes Sociales</h3>
          <p class="card-desc">Set de creatividades para campañas diarias en Instagram, Facebook y otras plataformas.</p>
          <div class="card-cta"><span class="card-cta-line"></span> Ver proyecto</div>
        </div>
      </a>

      <a class="project-card card-4 reveal" style="transition-delay:0.1s" href="project.html?id=4">
        <div class="card-bg"></div>
        <div class="card-num">04</div>
        <div class="card-tag">Google Ads</div>
        <div class="card-content">
          <div class="card-category">Publicidad Digital · DealerNET</div>
          <h3 class="card-title">Set de Animación — Google Ads</h3>
          <p class="card-desc">Piezas animadas diseñadas para campañas de display en la red de Google Ads. Múltiples formatos y tamaños.</p>
          <div class="card-cta"><span class="card-cta-line"></span> Ver proyecto</div>
        </div>
      </a>

      <a class="project-card card-5 reveal" style="transition-delay:0.2s" href="project.html?id=5">
        <div class="card-bg"></div>
        <div class="card-num">05</div>
        <div class="card-tag">META Ads</div>
        <div class="card-content">
          <div class="card-category">Publicidad Digital · DealerNET</div>
          <h3 class="card-title">Storyboard — META Ads</h3>
          <p class="card-desc">Guion visual para campañas en Facebook e Instagram, con especificaciones de animación y copy.</p>
          <div class="card-cta"><span class="card-cta-line"></span> Ver proyecto</div>
        </div>
      </a>

    </div>
  </section>

  <!-- SECTION BAR: 03 PROCESO -->
  <div class="section-bar" id="bar-proceso">
    <span class="section-bar-num">03</span>
    <div class="section-bar-line"></div>
    <span class="section-bar-label">Proceso</span>
  </div>

  <!-- PROCESO -->
  <section id="proceso">
    <div class="proceso-grid">
      <div class="proceso-intro reveal">
        <p class="section-label clip-reveal">Cómo trabajo</p>
        <h2 class="section-title clip-reveal delay-1">Del concepto a la pieza final.</h2>
        <p class="section-body" style="margin-top:1.5rem">
          Cada proyecto es un proceso de descubrimiento. Empiezo por entender profundamente la marca, el público y el
          objetivo — y de ahí construyo soluciones visuales que tienen sentido y que funcionan.
        </p>
        <div class="skills-cloud" style="margin-top:2.5rem">
          <span class="skill-tag">Figma</span>
          <span class="skill-tag">Adobe Illustrator</span>
          <span class="skill-tag">Photoshop</span>
          <span class="skill-tag">After Effects</span>
          <span class="skill-tag">Premiere Pro</span>
          <span class="skill-tag">InDesign</span>
          <span class="skill-tag">Google Ads</span>
          <span class="skill-tag">Meta Business</span>
        </div>
      </div>
      <ul class="steps-list reveal" style="transition-delay:0.15s">
        <li class="step-item">
          <span class="step-num">01</span>
          <div class="step-text">
            <h4>Descubrimiento</h4>
            <p>Entender la marca, el negocio y el público objetivo antes de diseñar una sola línea.</p>
          </div>
        </li>
        <li class="step-item">
          <span class="step-num">02</span>
          <div class="step-text">
            <h4>Estrategia Visual</h4>
            <p>Definir el lenguaje visual: paleta, tipografía, tono y estilo que diferencian a la marca.</p>
          </div>
        </li>
        <li class="step-item">
          <span class="step-num">03</span>
          <div class="step-text">
            <h4>Diseño &amp; Producción</h4>
            <p>Construir cada pieza con precisión técnica y atención obsesiva al detalle.</p>
          </div>
        </li>
        <li class="step-item">
          <span class="step-num">04</span>
          <div class="step-text">
            <h4>Entrega &amp; Documentación</h4>
            <p>Entregar assets listos para usar, con guías y manuales que permiten al cliente ser autónomo.</p>
          </div>
        </li>
      </ul>
    </div>
  </section>

  <!-- SECTION BAR: 04 ESTUDIO -->
  <div class="section-bar dark" id="bar-estudio">
    <span class="section-bar-num">04</span>
    <div class="section-bar-line"></div>
    <span class="section-bar-label">Estudio</span>
  </div>

  <!-- ESTUDIO -->
  <section id="estudio">
    <p class="section-label reveal clip-reveal">El estudio</p>
    <h2 class="section-title reveal clip-reveal delay-1" style="transition-delay:0.1s">Diseño con propósito,<br>forma con intención.</h2>
    <div class="studio-grid">
      <div class="studio-text reveal" style="transition-delay:0.2s">
        <blockquote class="studio-quote">
          "El buen diseño no es el que se ve bonito —<br>es el que <strong>resuelve</strong> algo."
        </blockquote>
        <div class="studio-meta">
          <div>
            <div class="studio-meta-label">Ubicación</div>
            <div class="studio-meta-val">Buenos Aires, Argentina</div>
          </div>
          <div style="margin-top:1.2rem">
            <div class="studio-meta-label">Disponibilidad</div>
            <div class="studio-meta-val">Proyectos freelance · Tiempo completo</div>
          </div>
          <div style="margin-top:1.2rem">
            <div class="studio-meta-label">Idiomas</div>
            <div class="studio-meta-val">Español · Inglés</div>
          </div>
        </div>
      </div>
      <div class="studio-visual reveal" style="transition-delay:0.3s">
        <div class="studio-visual-pattern"></div>
        <div class="studio-visual-center">
          <div class="studio-monogram">CN</div>
          <div class="studio-location">Buenos Aires · ARG</div>
        </div>
      </div>
    </div>
  </section>

  <!-- SECTION BAR: 05 CONTACTO -->
  <div class="section-bar" id="bar-contacto">
    <span class="section-bar-num">05</span>
    <div class="section-bar-line"></div>
    <span class="section-bar-label">Contacto</span>
  </div>

  <!-- CONTACTO -->
  <section id="contacto">
    <div class="contact-text reveal">
      <p class="section-label clip-reveal">¿Hablamos?</p>
      <h2 class="section-title clip-reveal delay-1">Empecemos algo juntos.</h2>
      <p class="section-body">
        Disponible para proyectos freelance, colaboraciones y posiciones de tiempo completo. Si tenés un proyecto en
        mente, escribime.
      </p>
      <div class="contact-links">
        <a href="mailto:camilo@ejemplo.com" class="contact-link">
          <span class="contact-link-label">Email</span>
          <span class="contact-link-val">camilo@ejemplo.com</span>
        </a>
        <a href="https://linkedin.com/in/camilonovillo" target="_blank" class="contact-link">
          <span class="contact-link-label">LinkedIn</span>
          <span class="contact-link-val">linkedin.com/in/camilonovillo</span>
        </a>
        <a href="https://behance.net/camilonovillo" target="_blank" class="contact-link">
          <span class="contact-link-label">Behance</span>
          <span class="contact-link-val">behance.net/camilonovillo</span>
        </a>
      </div>
    </div>
    <div class="contact-right reveal" style="transition-delay:0.2s">
      <div class="contact-cta-big">¡Hola!</div>
    </div>
  </section>

  <!-- FOOTER -->
  <footer>
    <p class="footer-copy">© 2024 Camilo Novillo — Diseñador Gráfico, Buenos Aires</p>
    <a href="#hero" class="footer-back">
      <span>↑</span> Volver al inicio
    </a>
  </footer>

  <script>
    // ─── PAGE CURTAIN REVEAL ─────────────────────────────
    const curtain = document.getElementById('page-curtain');
    window.addEventListener('load', () => {
      curtain.style.transition = 'transform 1s cubic-bezier(0.76, 0, 0.24, 1)';
      curtain.style.transformOrigin = 'top';
      setTimeout(() => { curtain.style.transform = 'scaleY(0)'; }, 80);
    });
    function navigateTo(url) {
      curtain.style.transition = 'transform 0.75s cubic-bezier(0.76, 0, 0.24, 1)';
      curtain.style.transformOrigin = 'bottom';
      curtain.style.transform = 'scaleY(0)';
      setTimeout(() => {
        curtain.style.transformOrigin = 'bottom';
        curtain.style.transform = 'scaleY(1)';
      }, 10);
      setTimeout(() => { window.location.href = url; }, 780);
    }

    // ─── PROJECT CARD TRANSITIONS ────────────────────────
    document.querySelectorAll('a.project-card').forEach(card => {
      card.addEventListener('click', e => {
        e.preventDefault();
        navigateTo(card.href);
      });
    });

    // ─── CURSOR ──────────────────────────────────────
    const cursor = document.getElementById('cursor');
    const ring = document.getElementById('cursor-ring');
    let mx = 0, my = 0, rx = 0, ry = 0;
    document.addEventListener('mousemove', e => { mx = e.clientX; my = e.clientY; });
    (function animRing() {
      rx += (mx - rx) * 0.12; ry += (my - ry) * 0.12;
      cursor.style.left = mx + 'px'; cursor.style.top = my + 'px';
      ring.style.left = rx + 'px'; ring.style.top = ry + 'px';
      requestAnimationFrame(animRing);
    })();
    document.querySelectorAll('a, button, .skill-tag').forEach(el => {
      el.addEventListener('mouseenter', () => cursor.classList.add('hovered'));
      el.addEventListener('mouseleave', () => cursor.classList.remove('hovered'));
    });

    // ─── HERO GLOW FOLLOWS MOUSE ────────────────────────
    const heroGlow = document.querySelector('.hero-glow');
    const hero = document.getElementById('hero');
    hero && document.addEventListener('mousemove', e => {
      const rect = hero.getBoundingClientRect();
      if (e.clientY < rect.bottom) {
        const x = (e.clientX / window.innerWidth) * 100;
        const y = (e.clientY / window.innerHeight) * 100;
        heroGlow.style.transform = `translate(${(x - 80) * 0.4}px, ${(y - 50) * 0.3}px)`;
      }
    });

    // ─── PARALLAX HERO TITLE ─────────────────────────
    const heroContent = document.querySelector('.hero-content');
    const heroBgGrid = document.querySelector('.hero-bg-grid');
    const nav = document.getElementById('main-nav');

    window.addEventListener('scroll', () => {
      const y = window.scrollY;
      if (heroContent) heroContent.style.transform = `translateY(${y * 0.25}px)`;
      if (heroBgGrid) heroBgGrid.style.transform = `translateY(${y * 0.1}px)`;
      nav.classList.toggle('scrolled', y > 60);
    }, { passive: true });

    // ─── INTERSECTION OBSERVER: reveal + clip-reveal + section bars ──
    const allReveal = document.querySelectorAll('.reveal, .clip-reveal');
    const revealObs = new IntersectionObserver(entries => {
      entries.forEach(e => { if (e.isIntersecting) e.target.classList.add('visible'); });
    }, { threshold: 0.1 });
    allReveal.forEach(el => revealObs.observe(el));

    // Section bars: trigger when they enter viewport
    const sectionBars = document.querySelectorAll('.section-bar');
    const barObs = new IntersectionObserver(entries => {
      entries.forEach(e => { if (e.isIntersecting) e.target.classList.add('bar-visible'); });
    }, { threshold: 0.3 });
    sectionBars.forEach(bar => barObs.observe(bar));

    // ─── ABOUT VISUAL KEN BURNS ──────────────────────
    const aboutVisualInner = document.querySelector('.about-visual-inner');
    if (aboutVisualInner) {
      aboutVisualInner.style.transition = 'transform 12s ease-in-out';
      aboutVisualInner.style.transformOrigin = 'center bottom';
      setTimeout(() => { aboutVisualInner.style.transform = 'scale(1.06)'; }, 800);
      setInterval(() => {
        aboutVisualInner.style.transform = aboutVisualInner.style.transform === 'scale(1.06)' ? 'scale(1)' : 'scale(1.06)';
      }, 12000);
    }
  </script>
</body>

</html>'''

with open('index.html', encoding='utf-8') as f:
    content = f.read()

# Find the head section end (</head>) and replace everything from <body> onwards
body_start = content.find('<body>')
if body_start == -1:
    print("ERROR: <body> not found")
else:
    head_part = content[:body_start]
    new_content = head_part + NEW_BODY
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"SUCCESS: wrote {len(new_content)} bytes, body starts at {body_start}")
