def get_mask_card_number(card_number: str) -> str:
    """
    маскирует номер банковской карты
    Пример: 8912292571489222 -> 8912 29** **** 9222
    """

    if len(card_number) < 16 or len(card_number) > 16:
        return "Номер карты состоит из 16 цифр."
    elif card_number.isdigit() is False:
        return "Номер карты состоит только из цифр"
    else:
        return (
            f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
        )


def get_mask_account(account_number: str) -> str:
    """
    принимает на вход номер счета и возвращает замаскированный номер
    Пример: 73654108430135874305 -> **4305
    """

    musk_account_number = []

    # убираем все символы, кроме последних шести
    for index, digit in enumerate(reversed(list(account_number))):
        if index < 4:
            musk_account_number.append(digit)

    # добавляем звездочки в начало маскировки
    musk_account_number.append("**")

    if 20 < len(account_number) < 20:
        return "Номер счета состоит из 20 цифр"
    elif account_number.isdigit() is False:
        return "Номер счета может состоять только из цифр"
    else:
        return "".join(reversed(musk_account_number))
