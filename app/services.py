import random

OPTIONS = ["Камень", "Ножницы", "Бумага"]


def play_rps(choice: str):
    computer_choice = random.choice(OPTIONS)

    if choice == computer_choice:
        return {
            "status": "success",
            "massage": "Ничья"
        }
    elif (choice == "Камень" and computer_choice == "Ножницы") or (
            choice == "Ножницы" and computer_choice == "Бумага") or (
            choice == "Бумага" and computer_choice == "Камень"):
        return {
            "status": "success",
            "massage": f"Ты выиграл! {choice} побеждает {computer_choice}"
        }
    else:
        return {
            "status": "success",
            "massage": f"Ты проиграл! {computer_choice} побеждает {choice}"
        }
