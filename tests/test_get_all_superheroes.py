from src.main import get_all_superheroes


def test_get_all_superheroes_response():
    result = get_all_superheroes()

    assert isinstance(result, list)
    assert len(result) > 0


def test_get_all_superheroes_structure():
    heroes = get_all_superheroes()
    hero = heroes[0]

    assert "name" in hero
    assert "appearance" in hero
    assert "work" in hero
    