from src.main import get_all_superheroes, get_tallest_superhero


def test_tallest_superhero_integration():
    heroes = get_all_superheroes()

    result = get_tallest_superhero(
        superheroes=heroes,
        gender="Male",
        has_work=True,
    )

    assert result is not None
    assert "name" in result
    assert "appearance" in result
