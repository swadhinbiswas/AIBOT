from bs4 import BeautifulSoup as bs
import requests
import json
import re

class TikTokDownloader:
    def __init__(self):
        self.url = "https://ssstik.io/en"
        self.headers = {
            "Accept": "application/json"
        }
        
    def download(self, url):
        response = requests.post(self.url, data={"url": url}, headers=self.headers)
        if response.status_code == 200:
            soup = bs(response.text, "html.parser")
            data = soup.find_all("script")
            data = data[1].string
            data = data.split("window.__NUXT__=")[1]
            data = data.split(";</script>")[0]
            data = json.loads(data)
            data = data["data"][0]
            data = data["video"]
            data = data["urls"]
            data = data[0]
            return data
        else:
            return None
          
    def download_without_watermark(self, url):
      
      
        response = requests.post(self.url, data={"url": url}, headers=self.headers)
        if response.status_code == 200:
            soup = bs(response.text, "html.parser")
            data = soup.find_all("script")
            data = data[1].string
            data = data.split("window.__NUXT__=")[1]
            data = data.split(";</script>")[0]
            data = json.loads(data)
            data = data["data"][0]
            data = data["video"]
            data = data["urls"]
            data = data[1]
            return data
        else:
            return None
          
          





x=TikTokDownloader()
print(x.download("https://www.tiktok.com/@emptiness945/video/737465"))