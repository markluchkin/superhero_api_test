import pytest

from src.main import get_tallest_superhero
from tests.test_data import TEST_SUPERHEROES


@pytest.mark.unit
def test_get_tallest_male_with_work():
    result = get_tallest_superhero(
        TEST_SUPERHEROES,
        gender="Male",
        has_work=True,
    )

    assert result["name"] == "Male 180"


@pytest.mark.unit
def test_get_tallest_male_without_work():
    result = get_tallest_superhero(
        TEST_SUPERHEROES,
        gender="Male",
        has_work=False,
    )

    assert result["name"] == "Male 190"


@pytest.mark.unit
def test_get_tallest_female_with_work():
    result = get_tallest_superhero(
        TEST_SUPERHEROES,
        gender="Female",
        has_work=True,
    )

    assert result["name"] == "Female 185"


@pytest.mark.unit
def test_get_tallest_female_without_work():
    result = get_tallest_superhero(
        TEST_SUPERHEROES,
        gender="Female",
        has_work=False,
    )

    assert result["name"] == "Female 170"


@pytest.mark.unit
def test_get_tallest_superhero_returns_none():
    result = get_tallest_superhero(
        TEST_SUPERHEROES,
        gender="Robot",
        has_work=True,
    )

    assert result is None


@pytest.mark.unit
def test_get_tallest_superhero_empty_list():
    result = get_tallest_superhero(
        superheroes=[],
        gender="Male",
        has_work=True
    )

    assert result is None