import requests
from functools import lru_cache

BASE_URL = "https://pokeapi.co/api/v2"

@lru_cache(maxsize=100)
def get_pokemon(name):
    response = requests.get(f"{BASE_URL}/pokemon/{name}")
    if response.status_code == 200:
        data = response.json()
        return {
            "name": data["name"],
            "id": data["id"],
            "types": [t["type"]["name"] for t in data["types"]],
            "abilities": [a["ability"]["name"] for a in data["abilities"]],
            "height": data["height"],
            "weight": data["weight"],
            "sprite": data["sprites"]["front_default"]  # Fetching the Pokemon image
        }
    return None
