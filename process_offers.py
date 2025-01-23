import requests
from urllib.parse import quote

url = "https://nodeapi.tueducaciondigital.site/newusuariosOffers"

# Hacer una solicitud GET a la URL para obtener el JSON
response = requests.get(url)
data = response.json()  # Convertir la respuesta a un diccionario de Python


# Iterar sobre todos los objetos en "data"
for item in data["data"]:
    print(f"Entrando al loop")
    fanpage = item["FanPage"]
    domain = item["Domain"]
    print(f"FanPage: {fanpage}")
    print(f"Domain: {domain}")

    # Encodear las URLs
    encoded_fanpage = quote(fanpage, safe='')
    encoded_domain = quote(domain, safe='')

    # Llamar a la API con la URL encodeada como query para fanpage
    api_url_fanpage = f"http://localhost:3005/getads?query={encoded_fanpage}"
    api_response_fanpage = requests.get(api_url_fanpage)
    api_data_fanpage = api_response_fanpage.json()
    activeAds_fanpage = api_data_fanpage["data"][0]["totalAds"]

    # Llamar a la API con la URL encodeada como query para domain
    api_url_domain = f"http://localhost:3005/getads?query={encoded_domain}"
    api_response_domain = requests.get(api_url_domain)
    api_data_domain = api_response_domain.json()
    activeAds_domain = api_data_domain["data"][0]["totalAds"]

    # Persistir el resultado para fanpage
    tracking_url = "https://nodeapi.tueducaciondigital.site/offersTracking"
    payload_fanpage = {
        "NumAds": activeAds_fanpage,
        "OffersFollo_ID": item["OffersFollo_ID"],
        "EnumAdsSourceCode": "FanPage"
    }
    response_fanpage = requests.post(tracking_url, json=payload_fanpage)
    print(f"Payload_fanpage: {payload_fanpage}")
    #print(f"Persisted FanPage data: {response_fanpage.status_code}")

    # Persistir el resultado para domain
    payload_domain = {
        "NumAds": activeAds_domain,
        "OffersFollo_ID": item["OffersFollo_ID"],
        "EnumAdsSourceCode": "Domain"
    }
    response_domain = requests.post(tracking_url, json=payload_domain)
    #print(f"Persisted Domain data: {response_domain.status_code}")

    #print(f"API Response for FanPage: {api_data_fanpage}")
    #print(f"API Response for Domain: {api_data_domain}")
