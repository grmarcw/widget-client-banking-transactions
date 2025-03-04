def mask_account_card(type_of_card_and_number_of_card: str) -> str:
    from scr import masks

    """обрабатывает информацию о картах и счетах"""
    type_of_card = []
    number_of_card = []

    # запуск итерации по вход. данным, чтобы разбить номер карты и ее тип
    for element in type_of_card_and_number_of_card:
        if element.isdigit():
            number_of_card.append(element)
        else:
            type_of_card.append(element)

    join_type = "".join(type_of_card).strip()
    join_number = "".join(number_of_card).strip()

    if "счет" in join_type.lower():
        if len(join_number) == 20:
            return f"{join_type} {masks.get_mask_account(join_number)}"
        else:
            return "Номер счета состоит из 20 цифр"
    elif join_type == "":
        return "Номер счета или карты не должен быть пустым"
    else:
        if len(join_number) == 16:
            return f"{join_type} {masks.get_mask_card_number(join_number)}"
        else:
            return "Номер карты состоит из 16 цифр."


def get_date(iso_str: str) -> str:
    """принимает формат iso(str), возвращает формат 'ДД.ММ.ГГГГ'(str)"""
    from datetime import datetime

    try:
        # iso-формат из строки переводим в datetime
        date_iso_object = datetime.fromisoformat(iso_str)
        # из iso-формата переводим в формат ДД.ММ.ГГГГ
        date_obj = date_iso_object.strftime("%d%m%Y")
        return f"{date_obj[:2]}.{date_obj[2:4]}.{date_obj[4:]}"
    except ValueError:
        return "Дата должна быть в формате 'iso'."
