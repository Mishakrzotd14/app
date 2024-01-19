from fastapi import APIRouter

from app.services import play_rps
from app.validators import validate_choice

router = APIRouter()


@router.get("/rps", tags=["rps"])
def get_rps(choice: str):
    correct_choice = validate_choice(choice)
    result_play = play_rps(correct_choice)
    return result_play
