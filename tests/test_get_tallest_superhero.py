from src.main import get_tallest_superhero, get_all_superheroes
from tests.test_data import TEST_SUPERHEROES


def test_get_tallest_male_with_work():
    result = get_tallest_superhero(
        TEST_SUPERHEROES,
        gender="Male",
        has_work=True,
    )

    assert result["name"] == "Male 180"


def test_get_tallest_male_without_work():
    result = get_tallest_superhero(
        TEST_SUPERHEROES,
        gender="Male",
        has_work=False,
    )

    assert result["name"] == "Male 190"


def test_get_tallest_female_with_work():
    result = get_tallest_superhero(
        TEST_SUPERHEROES,
        gender="Female",
        has_work=True,
    )

    assert result["name"] == "Female 185"


def test_get_tallest_female_without_work():
    result = get_tallest_superhero(
        TEST_SUPERHEROES,
        gender="Female",
        has_work=False,
    )

    assert result["name"] == "Female 170"


def test_get_tallest_superhero_returns_none():
    result = get_tallest_superhero(
        TEST_SUPERHEROES,
        gender="Robot",
        has_work=True,
    )

    assert result is None
