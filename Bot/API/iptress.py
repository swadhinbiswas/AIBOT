import requests

def trackip(ip:str):
    try:
        url=f"https://ipapi.co/{ip}/json/"
        
        response=requests.get(url)
        data=response.json()
        finaldata=f"""
        "ip": "{data['ip']}",
        "city": "{data['city']}",
        "region": "{data['region']}",
        "region_code": "{data['region_code']}",
        "country": "{data['country']}",
        "country_name": "{data['country_name']}",
        "continent_code": "{data['continent_code']}",
        "in_eu": "{data['in_eu']}",
        timezone": "{data['timezone']}",
        "utc_offset": "{data['utc_offset']}",
        "country_calling_code": "{data['country_calling_code']}",
        "currency": "{data['currency']}",
        "languages": "{data['languages']}",
        "asn": "{data['asn']}",
        "org": "{data['org']}"
        """
        return finaldata
        
    except Exception as e:
        return e

