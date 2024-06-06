import requests
import json


class UrlShortner:
    def __init__(self):
        self.url = "https://spoo.me"
        self.headers = {
    "Accept": "application/json"
}

        
    def shorten(self, url):
        
        
        """
        Shorten the given URL
        :param url: URL to shorten
        
        :return: Shortened URL
        
        """
        response = requests.post(self.url, data={"url": url}, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            return None
    
    def using_password(self, url, password):
        response = requests.post(self.url, data={"url": url, "password": password}, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            return None
      
    def using_custom_alias(self, url, alias):
        response = requests.post(self.url, data={"url": url, "custom_alias": alias}, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            return None
          
          

