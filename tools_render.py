import re,sys,subprocess,pathlib
src=pathlib.Path(sys.argv[1]); out=pathlib.Path(sys.argv[2]); title=sys.argv[3] if len(sys.argv)>3 else ""
s=src.read_text(encoding="utf-8")
# gabung baris label EDP dengan paragraf berikutnya supaya tidak terpisah halaman
s=re.sub(r'^(\[(?:FAKTA|OBSERVASI|HIPOTESIS[^\]]*|ASUMSI[^\]]*|TIDAK TAHU|FALSE REASON|DARK COGNITION[^\]]*|PLACEHOLDER[^\]]*)\])\n(?=\S)', r'<span class="lbl">\1</span>  \n', s, flags=re.M)
# baris bold berdiri sendiri (sub-judul) jadi h4 supaya nempel ke paragraf berikutnya
s=re.sub(r'^\*\*([^*\n]{3,70})\*\*$', r'#### \1', s, flags=re.M)
tmp=pathlib.Path("/tmp/_render.md"); tmp.write_text(s,encoding="utf-8")
css="""
@page{size:A4;margin:18mm 16mm 20mm 16mm}
body{font-family:"DejaVu Sans",sans-serif;font-size:10.5pt;line-height:1.45;color:#111}
h1{font-size:17pt;margin-top:0}
h2{font-size:13.5pt;margin-top:1.6em;page-break-after:avoid;break-after:avoid}
h3{font-size:11.5pt;margin-top:1.2em;page-break-after:avoid;break-after:avoid}
h4{font-size:10.5pt;margin:1em 0 0.3em 0;page-break-after:avoid;break-after:avoid}
h2.newpage{page-break-before:always}
p{orphans:3;widows:3;margin:0.45em 0;page-break-inside:avoid}
li{page-break-inside:avoid}
p:has(span.lbl){page-break-inside:avoid}
span.lbl{font-family:"DejaVu Sans Mono",monospace;font-size:9.5pt;font-weight:bold}
code{font-family:"DejaVu Sans Mono",monospace;font-size:9.2pt}
table{border-collapse:collapse;font-size:9.3pt;page-break-inside:avoid;margin:0.6em 0}
tr{page-break-inside:avoid}
td,th{border:1px solid #888;padding:3px 6px;vertical-align:top}
th{background:#eee}
div.keep{page-break-inside:avoid}
hr{border:0;border-top:1px solid #aaa;margin:1.2em 0}
blockquote{border-left:3px solid #999;margin:0.6em 0;padding-left:0.8em;color:#333}
"""
pathlib.Path("/tmp/_style.css").write_text(css)
html=subprocess.run(["pandoc",str(tmp),"-s","--css","/tmp/_style.css","--metadata","title=","-o","/tmp/_render.html"],capture_output=True)
h=pathlib.Path("/tmp/_render.html").read_text(encoding="utf-8")
# bab utama mulai halaman baru: h2 bernomor 1-5 dan LAMPIRAN A
h=re.sub(r'<h2 id="([^"]*)">((?:1|2|3|4|5)\. |LAMPIRAN A)', r'<h2 class="newpage" id="\1">\2', h)
# heading h3/h4 dibungkus bersama blok berikutnya supaya tidak jadi baris terakhir halaman
h=re.sub(r'(<h[234][^>]*>.*?</h[234]>\s*)((?:<h4[^>]*>.*?</h4>\s*)?(?:<p>.*?</p>|<table>.*?</table>|<ul>.*?</ul>|<ol>.*?</ol>))', r'<div class="keep">\1\2</div>', h, flags=re.S)
pathlib.Path("/tmp/_render.html").write_text(h,encoding="utf-8")
subprocess.run(["wkhtmltopdf","-q","--page-size","A4","--enable-local-file-access","--margin-top","22mm","--margin-bottom","20mm","--margin-left","16mm","--margin-right","16mm","--footer-center","[page] / [topage]","--footer-font-size","8","--footer-spacing","6",
  "--header-right",title,"--header-font-size","7","--header-spacing","6","/tmp/_render.html",str(out)])
print("ok",out)

# --- nomor halaman: overlay reportlab + pdftk multistamp ---
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
info=subprocess.run(["pdfinfo",str(out)],capture_output=True,text=True).stdout
n=int(re.search(r"Pages:\s+(\d+)",info).group(1))
c=canvas.Canvas("/tmp/_stamp.pdf",pagesize=A4); W,H=A4
for i in range(1,n+1):
    c.setFont("Helvetica",8); c.drawCentredString(W/2,26,f"{i} / {n}")
    if title: c.drawRightString(W-45,H-32,title)
    c.showPage()
c.save()
subprocess.run(["pdftk",str(out),"multistamp","/tmp/_stamp.pdf","output","/tmp/_stamped.pdf"],check=True)
pathlib.Path("/tmp/_stamped.pdf").replace(out); print("stamped",n,"pages")
