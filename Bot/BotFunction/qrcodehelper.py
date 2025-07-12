import qrcode
from qrcode.constants import ERROR_CORRECT_H
from PIL import Image, ImageDraw
from qrcode.image.pil import PilImage
import json
import os
import requests

jsonfile = os.path.join(os.path.dirname(__file__), "qrcodeicon.json")
iconfolder = os.path.join(os.path.dirname(__file__), "icon")
os.makedirs(iconfolder, exist_ok=True)

with open(jsonfile, "r") as f:
    data = json.load(f)

def download_icon(domain: str, path: str):
    url = data.get(domain, "")
    if not url:
        url = "https://cdn.icon-icons.com/icons2/2699/PNG/512/python_logo_icon_168886.png"
    response = requests.get(url, stream=True)
    with open(path, "wb") as f:
        for chunk in response.iter_content(chunk_size=128):
            f.write(chunk)

def make_rounded_icon(img: Image.Image, size: int) -> Image.Image:
    img = img.convert("RGBA")
    img = img.resize((size, size), Image.Resampling.LANCZOS)
    mask = Image.new("L", (size, size), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, size, size), fill=255)
    img.putalpha(mask)
    return img

def createqr(url: str) -> str:
    try:
        domain = url.split(".")[1]
    except IndexError:
        domain = "default"

    icon_path = os.path.join(iconfolder, "icon.png")
    download_icon(domain, icon_path)

    icon = Image.open(icon_path)
    qr = qrcode.QRCode(
        version=1,
        error_correction=ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white", image_factory=PilImage).convert("RGB")
    qr_img = qr.make_image(fill_color="black", back_color="white").convert("RGB")

    # Resize and mask icon
    icon_size = qr_img.size[0] // 4  # 25% of QR size
    icon = make_rounded_icon(icon, icon_size)

    # Paste icon into QR
    pos = ((qr_img.size[0] - icon_size) // 2, (qr_img.size[1] - icon_size) // 2)
    qr_img.paste(icon, pos, icon)

    output_path = os.path.join(iconfolder, "qrcode.png")
    qr_img.save(output_path)
    return output_path
