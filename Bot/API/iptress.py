import requests

def trackip(ip:str):
    try:
        url=f"https://ipapi.co/{ip}/json/"

        response=requests.get(url)
        data=response.json()
        finaldata = {
            "ip": data.get('ip'),
            "city": data.get('city'),
            "region": data.get('region'),
            "region_code": data.get('region_code'),
            "country": data.get('country'),
            "country_name": data.get('country_name'),
            "continent_code": data.get('continent_code'),
            "in_eu": data.get('in_eu'),
            "timezone": data.get('timezone'),
            "utc_offset": data.get('utc_offset'),
            "country_calling_code": data.get('country_calling_code'),
            "currency": data.get('currency'),
            "languages": data.get('languages'),
            "asn": data.get('asn'),
            "org": data.get('org')
        }
        return finaldata

    except Exception as e:
        return e
