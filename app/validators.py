from fastapi import HTTPException

OPTIONS = ["Камень", "Ножницы", "Бумага"]


def validate_choice(choice: str):
    if choice.capitalize() in OPTIONS:
        return choice.capitalize()
    else:
        raise HTTPException(status_code=400,
                            detail={
                                "status": "error",
                                "massage": f"Параметр {choice} принимает"
                                           f"значения 'Камень', 'Ножницы',"
                                           f"'Бумага'. Ты передал - {choice}"
                            })
