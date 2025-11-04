import requests

TOKEN = "b6499ca52d5fc1"  # your ipinfo token

def get_location():
    url = f"https://ipinfo.io/json?token={TOKEN}"
    response = requests.get(url)
    data = response.json()
    
    city_now = data.get('city')
    loc = data.get('loc', '')
    lat, lon = map(float, loc.split(',')) if loc else (None, None)

    print("City:", city_now)
    print("Latitude:", lat)
    print("Longitude:", lon)

    return city_now, lat, lon

# Example usage
get_location()
