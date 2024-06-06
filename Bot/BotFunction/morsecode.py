from requests import get

def morsecode(text):
    url = f"https://api.funtranslations.com/translate/morse.json?text={text}"
    response = get(url)
    if response.status_code == 200:
        return response.json()['contents']['translated']
    else:
        return "Error"
      
      



x=morsecode("Hello World")

print(x)