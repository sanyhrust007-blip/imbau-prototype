"""Збирає сторінки демо для GitHub Pages з ../prototype/imbau-demo.html.

На кожну сторінку ставить код Google Tag Manager (GTM-MGCF55BB).
index.html = те саме демо + noindex. Запуск: python -I publish.py
"""
from pathlib import Path

GTM_ID = "GTM-MGCF55BB"
HEAD = f"""<meta charset="utf-8">
<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){{w[l]=w[l]||[];w[l].push({{'gtm.start':
new Date().getTime(),event:'gtm.js'}});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
}})(window,document,'script','dataLayer','{GTM_ID}');</script>
<!-- End Google Tag Manager -->
"""
BODY = f"""<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id={GTM_ID}"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->
"""
NOINDEX = '<meta name="robots" content="noindex,nofollow">\n'

here = Path(__file__).parent
demo = (here.parent / "prototype" / "imbau-demo.html").read_text(encoding="utf-8")
assert "googletagmanager" not in demo, "у зібраному демо вже є GTM"
# скрипт GTM має стояти раніше за інші <script>, тому вставляємо на самий початок документа
for name, extra in (("imbau-demo.html", ""), ("index.html", NOINDEX)):
    (here / name).write_text(HEAD + extra + BODY + demo, encoding="utf-8")
    print("ok", name)
