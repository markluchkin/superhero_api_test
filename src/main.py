import requests
from typing import Optional, Any

from src.config import API_URL


def get_all_superheroes() -> list[dict[str, Any]]:
    try:
        response = requests.get(API_URL, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        raise RuntimeError(f"Failed: {e}")
    

def get_superhero_height(superhero: dict[str, Any]) -> int:
    height = superhero["appearance"]["height"][1]
    if height.endswith(" cm"):
        return int(height.replace(" cm", ""))
    if height.endswith(" meters"):
        return int(float(height.replace(" meters", "")) * 100)
    
    return 0


def has_work_status(superhero: dict[str, Any]) -> bool:
    occupation = superhero["work"]["occupation"]

    return bool(occupation and occupation != "-" and occupation.strip())


def get_tallest_superhero(superheroes: list, gender: str, has_work: bool) -> Optional[dict[str, Any]]:
    filtered_superheroes = [
        superhero for superhero in superheroes 
        if superhero["appearance"]["gender"] == gender
        and has_work_status(superhero=superhero) == has_work
    ]

    if not filtered_superheroes:
        return None

    return max(filtered_superheroes, key=get_superhero_height)
