import generators.generators


def test_filter_by_currency(
    dictionary_list: list, filter_rus: list, filter_usd: list
) -> None:
    rus = []
    usd = []
    kz = []
    wtf: list = []

    for element in generators.generators.filter_by_currency(
        dictionary_list, "RUS"
    ):
        rus.append(element)

    for element in generators.generators.filter_by_currency(
        dictionary_list, "USD"
    ):
        usd.append(element)

    for element in generators.generators.filter_by_currency(
        dictionary_list, "KZ"
    ):
        kz.append(element)

    for element in generators.generators.filter_by_currency([], "KZ"):
        kz.append(element)

    assert rus == filter_rus
    assert usd == filter_usd
    assert kz == []
    assert wtf == []


def test_transaction_descriptions(dictionary_list: list) -> None:
    correct_description_list = [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод организации",
        "Перевод организации",
    ]
    test_description_list = []
    test_description_list_part_two = []

    for elem in generators.generators.transaction_descriptions(
        dictionary_list
    ):
        test_description_list.append(elem)

    for elem in generators.generators.transaction_descriptions([]):
        test_description_list_part_two.append(elem)

    assert test_description_list == correct_description_list
    assert test_description_list_part_two == []


def test_card_number_generator() -> None:
    card_number = generators.generators.card_number_generator(0, 4)
    assert next(card_number) == "0000 0000 0000 0000"
    assert next(card_number) == "0000 0000 0000 0001"
    assert next(card_number) == "0000 0000 0000 0002"
    assert next(card_number) == "0000 0000 0000 0003"
    assert next(card_number) == "0000 0000 0000 0004"
