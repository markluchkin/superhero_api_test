import requests
from typing import Optional, Dict, Any

from config import API_URL


def get_all_superheroes() -> list:
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        raise Exception(f"Error: {e}")


def get_tallest_superhero(gender: str, has_work: bool) -> Optional[Dict[str, Any]]:
    pass
