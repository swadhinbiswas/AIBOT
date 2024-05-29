import os 
import json

filepath = os.path.join(os.path.dirname(__file__), "qrcodeicon.json")


def get_qrcodeicon(text):
    split_text = text.split(".")
    with open(filepath, "r") as f:
        data = json.load(f)
        if split_text[1] in data:
            return data[split_text[1]]
          
          

def set_qricon(text:str,icon:str):
    split_text = text.split(".")
    with open(filepath, "r") as f:
        data = json.load(f)
        data[split_text[1]] = icon
    with open(filepath, "w") as f:
        json.dump(data, f, indent=4)