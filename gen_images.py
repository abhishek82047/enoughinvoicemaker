import base64
import os

def get_b64(path):
    if not os.path.exists(path): return ""
    ext = path.split(".")[-1].lower()
    mime = "image/png" if ext == "png" else "image/jpeg"
    with open(path, "rb") as f:
        return f"data:{mime};base64," + base64.b64encode(f.read()).decode()

logo = get_b64("favicon.png")
qr = get_b64("qrcode.jpeg")

with open("images.js", "w", encoding="utf-8") as f:
    f.write(f"const LOGO_B64 = '{logo}';\n")
    f.write(f"const QR_B64 = '{qr}';\n")
