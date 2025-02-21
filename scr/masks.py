def get_mask_card_number(card_number: str) -> str:
    """маскирует номер банковской карты"""

    mask_card_number = []

    four_digits_to_divide_blocks = 0

    # делим номер карты на 4 блока
    for digit in card_number:
        four_digits_to_divide_blocks += 1
        if four_digits_to_divide_blocks % 4 == 0:
            mask_card_number.append(digit)
            mask_card_number.append(" ")
        else:
            mask_card_number.append(digit)

    # маскируем часть номера карты
    for index, digit in enumerate(mask_card_number):
        if index < 14 and index > 6 and digit != " ":
            mask_card_number[index] = "*"

    return "".join(mask_card_number)


def get_mask_account(account_number: str) -> str:
    """принимает на вход номер счета и возвращает замаскированный номер"""

    musk_account_number = []

    # убираем все символы, кроме последних шести
    for index, digit in enumerate(reversed(list(account_number))):
        if index < 4:
            musk_account_number.append(digit)

    # добавляем звездочки в начало маскировки
    musk_account_number.append("**")

    return "".join(reversed(musk_account_number))
