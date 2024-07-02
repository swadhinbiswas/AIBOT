import requests
from Bot.settings.setting import settings
import os



pdfolder=os.path.join(os.path.dirname(__file__), "pdf")
def html_to_pdf(url:str):
 baseurl=f"""https://api.html2pdf.app/v1/generate?html={url}&apiKey={settings.HTML2PDF_API_KEY}"""
 
 responce=requests.get(baseurl)
 with open(f"{pdfolder}/pdf.pdf", "wb") as f:
   
   
    f.write(responce.content)
    
  
   
 return f"{pdfolder}/pdf.pdf"





