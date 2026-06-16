import requests
from typing import Optional, Dict, Any

from config import API_URL


def get_all_superheroes() -> list:
    response = requests.get(API_URL)
    response.raise_for_status()
    return response.json()
    

def get_superhero_height(superhero: Dict[str, Any]) -> int:
    height = superhero["appearance"]["height"][1]
    return int(height.replace(" cm", ""))


def get_tallest_superhero(gender: str, has_work: bool) -> Optional[Dict[str, Any]]:
    superheroes = get_all_superheroes()
    filtered_superheroes = []
