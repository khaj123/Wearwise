"""Build a single self-contained HTML version with embedded images (Python 3, no packages)."""
from pathlib import Path
import base64, json
root = Path(__file__).resolve().parent
assets = {f.stem: 'data:image/jpeg;base64,' + base64.b64encode(f.read_bytes()).decode('ascii') for f in (root/'assets').glob('*.jpg')}
html = (root/'index.html').read_text(encoding='utf-8')
html = html.replace('<link rel="stylesheet" href="styles.css">', '<style>' + (root/'styles.css').read_text(encoding='utf-8') + '</style>')
html = html.replace('<script src="app.js"></script>', '<script>window.WEARWISE_ASSETS=' + json.dumps(assets) + ';</script><script>' + (root/'app.js').read_text(encoding='utf-8') + '</script>')
(root/'Wearwise_Prototype.html').write_text(html, encoding='utf-8')
print('Created Wearwise_Prototype.html')
