with open('index.html', encoding='utf-8') as f:
    c = f.read()

js_start = c.rfind('<script>')
js_section = c[js_start:]
print(f'JS length: {len(js_section)} chars')
# Print first 3000 chars of JS
print(js_section[:3000])
