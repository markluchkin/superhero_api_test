import requests
from typing import Optional, Dict, Any

from config import API_URL


def get_all_superheroes() -> list:
    response = requests.get(API_URL)
    response.raise_for_status()
    return response.json()
    

def get_superhero_height(superhero: Dict[str, Any]) -> int:
    height = superhero["appearance"]["height"][1]
    if height.endswith(" cm"):
        return int(height.replace(" cm", ""))
    if height.endswith(" meters"):
        return int(float(height.replace(" meters", "")) * 100)
    
    return 0


def has_work_status(superhero: Dict[str, Any]) -> bool:
    occupation = superhero["work"]["occupation"]

    return bool(occupation and occupation != "-" and occupation.strip()) # .strip() для случаев occupation = "   "


def get_tallest_superhero(gender: str, has_work: bool) -> Optional[Dict[str, Any]]:
    superheroes = get_all_superheroes()

    filtered_superheroes = [
        superhero for superhero in superheroes 
        if superhero["appearance"]["gender"] == gender
        and has_work_status(superhero=superhero) == has_work
    ]

    return max(filtered_superheroes, key=get_superhero_height)
