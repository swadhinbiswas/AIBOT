import requests
from Bot.settings.setting import settings
import os



pdfolder = os.path.join(os.path.dirname(__file__), "pdf")

def html_to_pdf(url: str):
    baseurl = f"https://api.html2pdf.app/v1/generate?html={url}&apiKey={settings.HTML2PDF_API_KEY}"
    response = requests.get(baseurl)
    os.makedirs(pdfolder, exist_ok=True)
    with open(f"{pdfolder}/pdf.pdf", "wb") as f:
        f.write(response.content)
    return f"{pdfolder}/pdf.pdf"
