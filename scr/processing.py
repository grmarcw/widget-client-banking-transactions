def filter_by_state(list_dict: list, option_value: str = "EXECUTED") -> list:
    """
    на основе старого списка словарей создает новый,
    в которых ключ 'state' равняется указанному значению
    (по умолчанию = 'EXECUTED')
    """
    # создаем новый список для словарей,
    # в которых значения ключа 'state' = указанному значению
    new_list = []

    for dictionary in list_dict:
        if dictionary.get("state") == option_value:
            new_list.append(dictionary)

    return new_list


def sort_by_date(list_dict: list, is_sorting_order: bool = True) -> list:
    """сортирует принимаемый список по дате(по умолчанию убывание)"""
    from datetime import datetime

    sorted_list_dict = sorted(
        list_dict,
        key=lambda x: datetime.fromisoformat(x["date"]),
        reverse=not is_sorting_order,
    )

    return sorted_list_dict
