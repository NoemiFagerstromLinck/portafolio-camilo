with open('index.html', encoding='utf-8') as f:
    content = f.read()

print('Has proj1.png already:', 'proj1.png' in content)

card_css = (
    '\n    /* card bg images */\n'
    '    .card-bg { background-size: cover !important; background-position: center top !important; }\n'
    '    .card-1 .card-bg { background-image: url("img/proj1.png") !important; }\n'
    '    .card-2 .card-bg { background-image: url("img/proj2.png") !important; }\n'
    '    .card-3 .card-bg { background-image: url("img/proj3.png") !important; }\n'
    '    .card-4 .card-bg { background-image: url("img/proj4.png") !important; }\n'
    '    .card-5 .card-bg { background-image: url("img/proj5.png") !important; }\n'
    '    .card-bg::after {\n'
    '      content: "";\n'
    '      position: absolute;\n'
    '      inset: 0;\n'
    '      background: linear-gradient(160deg, rgba(0,0,0,0.65) 0%, rgba(0,0,0,0.2) 100%);\n'
    '      z-index: 0;\n'
    '    }\n'
    '    /* clip-path card expand animation */\n'
    '    .project-card.reveal {\n'
    '      opacity: 1 !important;\n'
    '      transform: none !important;\n'
    '      clip-path: inset(0 100% 0 0);\n'
    '      transition: clip-path 0.95s cubic-bezier(0.16, 1, 0.3, 1) !important;\n'
    '    }\n'
    '    .project-card.reveal.visible { clip-path: inset(0 0% 0 0) !important; }\n'
    '    /* section label clip reveal */\n'
    '    .clip-reveal { clip-path: inset(0 100% 0 0); transition: clip-path 1s cubic-bezier(0.16,1,0.3,1); }\n'
    '    .clip-reveal.visible { clip-path: inset(0 0% 0 0); }\n'
    '    .clip-reveal.delay-1 { transition-delay: 0.15s; }\n'
    '    .clip-reveal.delay-2 { transition-delay: 0.3s; }\n'
)

# Find last </style> and insert before it
idx = content.rfind('</style>')
if idx >= 0 and 'proj1.png' not in content:
    content = content[:idx] + card_css + '  </style>' + content[idx + len('</style>'):]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print('DONE. CSS injected at idx', idx)
    print('Verify proj1.png present:', 'proj1.png' in content)
elif 'proj1.png' in content:
    print('Already patched, skipping.')
else:
    print('ERROR: no </style> found!')
