from fastapi import HTTPException

from app.validators import validate_choice


def test_validate_choice_valid():
    choice = "Камень"
    assert validate_choice(choice) == choice.capitalize()


def test_validate_choice_invalid():
    invalid_choice = "Колодец"
    try:
        validate_choice(invalid_choice)
    except HTTPException as e:
        assert e.status_code == 400
        assert "Параметр" in e.detail["massage"]
        assert invalid_choice in e.detail["massage"]
