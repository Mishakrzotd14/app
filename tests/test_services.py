from app.services import play_rps


def test_play_rps():
    for option in ["Камень", "Ножницы", "Бумага"]:
        result = play_rps(option)
        assert "status" in result
        assert "massage" in result
