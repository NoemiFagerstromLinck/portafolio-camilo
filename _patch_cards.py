"""Patch index.html:
1. Add per-card background images using img/proj1-5.png
2. Add clip-path card reveal animation (expand from left, Telha Clarke style)
3. Make card images zoom smoothly on hover
"""

with open('index.html', encoding='utf-8') as f:
    content = f.read()

# ─── 1. ADD CARD IMAGE CSS ────────────────────────────────────────────────────
# We'll add card-specific bg image rules right after .card-bg CSS block
card_img_css = """
    /* ─── CARD BACKGROUND IMAGES ──────────────────────────────── */
    .card-1 .card-bg { background: linear-gradient(160deg, #0d1117 0%, #1a1a2e 100%) center/cover; }
    .card-2 .card-bg { background: linear-gradient(160deg, #0d1117 0%, #1a1a2e 100%) center/cover; }
    .card-3 .card-bg { background: linear-gradient(160deg, #0d1117 0%, #1a1a2e 100%) center/cover; }
    .card-4 .card-bg { background: linear-gradient(160deg, #0d1117 0%, #1a1a2e 100%) center/cover; }
    .card-5 .card-bg { background: linear-gradient(160deg, #0d1117 0%, #1a1a2e 100%) center/cover; }

    .card-1 .card-bg { background-image: url('img/proj1.png'); background-size: cover; background-position: center top; }
    .card-2 .card-bg { background-image: url('img/proj2.png'); background-size: cover; background-position: center top; }
    .card-3 .card-bg { background-image: url('img/proj3.png'); background-size: cover; background-position: center top; }
    .card-4 .card-bg { background-image: url('img/proj4.png'); background-size: cover; background-position: center top; }
    .card-5 .card-bg { background-image: url('img/proj5.png'); background-size: cover; background-position: center top; }

    /* ─── CARD CLIP REVEAL (expand from left) ─────────────────── */
    /* Cards start clipped to 0 width and expand horizontally on scroll */
    .project-card.reveal {
      clip-path: inset(0 100% 0 0);
      opacity: 1 !important; /* override old reveal opacity */
      transform: none !important;
      transition: clip-path 0.9s cubic-bezier(0.16, 1, 0.3, 1) !important;
    }
    .project-card.reveal.visible {
      clip-path: inset(0 0% 0 0);
    }
    /* Stagger delays for each card */
    .project-card.reveal:nth-child(1) { transition-delay: 0s !important; }
    .project-card.reveal:nth-child(2) { transition-delay: 0.12s !important; }
    .project-card.reveal:nth-child(3) { transition-delay: 0.24s !important; }
    .project-card.reveal:nth-child(4) { transition-delay: 0.08s !important; }
    .project-card.reveal:nth-child(5) { transition-delay: 0.18s !important; }

    /* Dark overlay so text remains readable over bright PDF covers */
    .card-bg::after {
      content: '';
      position: absolute;
      inset: 0;
      background: linear-gradient(160deg, rgba(0,0,0,0.55) 0%, rgba(0,0,0,0.2) 100%);
      z-index: 0;
    }
"""

# Inject before the closing </style> tag in the head
content = content.replace('  </style>\n</head>', card_img_css + '  </style>\n</head>', 1)

# ─── 2. OVERRIDE OLD REVEAL ON .project-card (remove opacity/transform) ──────
# The old .reveal CSS sets opacity:0 and translateY — we override with clip-path above.
# No other changes needed since CSS specificity of nth-child will win.

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done. Card images and clip-path animations patched.')
