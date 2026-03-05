"""
Fix the reveal animations:
1. Remove clip-path from project-card.reveal (causes invisible cards on scroll miss)
2. Use translateX + opacity instead (horizontal slide-in which is also "se agrandaba hacia los lados")  
3. Add rootMargin to IntersectionObserver so elements start revealing earlier
4. Fix clip-reveal on labels to be slide-up instead of clip-path (more compatible)
"""

with open('index.html', encoding='utf-8') as f:
    content = f.read()

# Check current state
has_old_clip = 'clip-path: inset(0 100% 0 0)' in content
print(f'Has clip-path animation: {has_old_clip}')
print(f'Has proj1.png: {"proj1.png" in content}')

# Replace the clip-path card reveal approach with translateX slide
# Find and replace our previously injected card animation CSS
old_card_anim = (
    '    /* clip-path card expand animation */\n'
    '    .project-card.reveal {\n'
    '      opacity: 1 !important;\n'
    '      transform: none !important;\n'
    '      clip-path: inset(0 100% 0 0);\n'
    '      transition: clip-path 0.95s cubic-bezier(0.16, 1, 0.3, 1) !important;\n'
    '    }\n'
    '    .project-card.reveal.visible { clip-path: inset(0 0% 0 0) !important; }\n'
)

new_card_anim = (
    '    /* card horizontal slide-in animation (se agrandaba hacia los lados) */\n'
    '    .project-card.reveal {\n'
    '      opacity: 0;\n'
    '      transform: translateX(-40px) scale(0.97);\n'
    '      transition: opacity 0.8s ease, transform 0.8s cubic-bezier(0.16,1,0.3,1) !important;\n'
    '    }\n'
    '    .project-card.reveal.visible {\n'
    '      opacity: 1;\n'
    '      transform: translateX(0) scale(1);\n'
    '    }\n'
    '    .project-card.reveal:nth-child(2) { transition-delay: 0.1s !important; }\n'
    '    .project-card.reveal:nth-child(3) { transition-delay: 0.2s !important; }\n'
    '    .project-card.reveal:nth-child(4) { transition-delay: 0.1s !important; }\n'
    '    .project-card.reveal:nth-child(5) { transition-delay: 0.2s !important; }\n'
)

old_clip_reveal = (
    '    /* section label clip reveal */\n'
    '    .clip-reveal { clip-path: inset(0 100% 0 0); transition: clip-path 1s cubic-bezier(0.16,1,0.3,1); }\n'
    '    .clip-reveal.visible { clip-path: inset(0 0% 0 0); }\n'
    '    .clip-reveal.delay-1 { transition-delay: 0.15s; }\n'
    '    .clip-reveal.delay-2 { transition-delay: 0.3s; }\n'
)

new_clip_reveal = (
    '    /* section label clip reveal - slide up from below */\n'
    '    .clip-reveal { opacity: 0; transform: translateY(20px); transition: opacity 0.7s ease, transform 0.7s cubic-bezier(0.16,1,0.3,1); }\n'
    '    .clip-reveal.visible { opacity: 1; transform: translateY(0); }\n'
    '    .clip-reveal.delay-1 { transition-delay: 0.15s; }\n'
    '    .clip-reveal.delay-2 { transition-delay: 0.3s; }\n'
)

if old_card_anim in content:
    content = content.replace(old_card_anim, new_card_anim)
    print('Replaced card animation CSS')
else:
    # Try to find it differently by looking for clip-path line
    import re
    # Add it before end of style if not found
    content = content.replace('  </style>', new_card_anim + '  </style>', 1)
    print('Appended card animation CSS (original not found exactly)')

if old_clip_reveal in content:
    content = content.replace(old_clip_reveal, new_clip_reveal)
    print('Replaced clip-reveal CSS')
else:
    print('clip-reveal CSS not found with exact match, skipping')

# Also fix the IntersectionObserver to use rootMargin so it fires earlier
old_observer = (
    '    const allReveal = document.querySelectorAll(\'.reveal, .clip-reveal\');\n'
    '    const revealObs = new IntersectionObserver(entries => {\n'
    '      entries.forEach(e => { if (e.isIntersecting) e.target.classList.add(\'visible\'); });\n'
    '    }, { threshold: 0.1 });\n'
    '    allReveal.forEach(el => revealObs.observe(el));'
)

new_observer = (
    '    const allReveal = document.querySelectorAll(\'.reveal, .clip-reveal\');\n'
    '    const revealObs = new IntersectionObserver(entries => {\n'
    '      entries.forEach(e => { if (e.isIntersecting) e.target.classList.add(\'visible\'); });\n'
    '    }, { threshold: 0.08, rootMargin: \'0px 0px -60px 0px\' });\n'
    '    allReveal.forEach(el => revealObs.observe(el));'
)

if old_observer in content:
    content = content.replace(old_observer, new_observer)
    print('Updated IntersectionObserver rootMargin')
else:
    print('IntersectionObserver not found with exact match')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print(f'Done. File size: {len(content)} bytes')
