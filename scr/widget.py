def mask_account_card(type_of_card_and_number_of_card: str) -> str:
    import masks
    """обрабатывает информацию о картах и счетах"""
    type_of_card = []
    number_of_card = []

    # запуск итерации по вход. данным, чтобы разбить номер карты и ее тип
    for element in type_of_card_and_number_of_card:
        if element.isdigit():
            number_of_card.append(element)
        else:
            type_of_card.append(element)

    join_type = ''.join(type_of_card)
    join_number = ''.join(number_of_card)

    if join_type == 'Счет ':
        return f'{join_type} {masks.get_mask_account(join_number)}'
    else:
        return f'{join_type} {masks.get_mask_card_number(join_number)}'

def get_date(iso_str: str) -> str:
    """принимает формат iso(str), возвращает формат 'ДД.ММ.ГГГГ'(str)"""
    from datetime import datetime

    # iso-формат из строки переводим в datetime
    date_iso_object = datetime.fromisoformat(iso_str)
    # из iso-формата переводим в формат ДД.ММ.ГГГГ
    date_obj = date_iso_object.strftime('%d%m%Y')

    return f'{date_obj[:2]}.{date_obj[2:4]}.{date_obj[4:]}'
