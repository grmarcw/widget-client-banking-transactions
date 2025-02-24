def filter_by_state(list_dict: list, option_value: str = "EXECUTED") -> list:
    """
    на основе старого списка словарей создает новый,
    в которых ключ 'state' равняется указанному значению(по умолчанию = 'EXECUTED')
    """
    # создаем новый список для словарей, в которых значения ключа 'state' будет равняться указанному значению
    new_list = []

    for dictionary in list_dict:
        if dictionary.get("state") == option_value:
            new_list.append(dictionary)

    return new_list
