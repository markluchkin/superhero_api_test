import pytest

from src.main import get_superhero_height


@pytest.mark.unit
def test_get_superhero_height_cm():
    superhero = {
        "appearance": {
            "height": ["", "188 cm"]
        }
    }

    assert get_superhero_height(superhero) == 188


@pytest.mark.unit
def test_get_superhero_height_meters():
    superhero = {
        "appearance": {
            "height": ["", "15.2 meters"]
        }
    }

    assert get_superhero_height(superhero) == 1520


@pytest.mark.unit
def test_get_superhero_height_unknown_format():
    superhero = {
        "appearance": {
            "height": ["", "unknown"]
        }
    }

    assert get_superhero_height(superhero) == 0