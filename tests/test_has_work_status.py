from src.main import has_work_status


def test_has_work_status_true():
    superhero = {
        "work": {
            "occupation": "something"
        }
    }

    assert has_work_status(superhero) is True


def test_has_work_status_false_dash():
    superhero = {
        "work": {
            "occupation": "-"
        }
    }

    assert has_work_status(superhero) is False


def test_has_work_status_false_empty():
    superhero = {
        "work": {
            "occupation": ""
        }
    }

    assert has_work_status(superhero) is False


def test_has_work_status_false_spaces():
    superhero = {
        "work": {
            "occupation": "   "
        }
    }

    assert has_work_status(superhero) is False