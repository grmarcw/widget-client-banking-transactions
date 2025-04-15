import pytest

from scr import generators


@pytest.mark.parametrize(
    "currency, result",
    [
        (
            "RUS",
            [
                {
                    "id": 123456789,
                    "state": "EXECUTED",
                    "date": "2029-04-04T23:20:05.206878",
                    "operationAmount": {
                        "amount": "79114.93",
                        "currency": {"name": "RUS", "code": "RUS"},
                    },
                    "description": "Перевод организации",
                    "from": "Счет 19708645243283128599",
                    "to": "Счет 75651667383060281234",
                },
                {
                    "id": 987654321,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                    "operationAmount": {
                        "amount": "9824.07",
                        "currency": {"name": "RUS", "code": "RUS"},
                    },
                    "description": "Перевод организации",
                    "from": "Счет 75106830611234567890",
                    "to": "Счет 11776614600987654321",
                },
            ],
        ),
        (
            "USD",
            [
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                    "operationAmount": {
                        "amount": "9824.07",
                        "currency": {"name": "USD", "code": "USD"},
                    },
                    "description": "Перевод организации",
                    "from": "Счет 75106830613657916952",
                    "to": "Счет 11776614605963066702",
                },
                {
                    "id": 142264268,
                    "state": "EXECUTED",
                    "date": "2019-04-04T23:20:05.206878",
                    "operationAmount": {
                        "amount": "79114.93",
                        "currency": {"name": "USD", "code": "USD"},
                    },
                    "description": "Перевод со счета на счет",
                    "from": "Счет 19708645243227258542",
                    "to": "Счет 75651667383060284188",
                },
            ],
        ),
        ("KZ", []),
    ],
)
def test_filter_by_currency(
    dictionary_list: list, currency: str, result: list
) -> None:
    new_dict_list = []
    none_list = []

    for element in generators.filter_by_currency(
        dictionary_list, currency
    ):
        new_dict_list.append(element)

    for element in generators.filter_by_currency([], currency):
        none_list.append(element)

    assert new_dict_list == result
    assert none_list == []


def test_transaction_descriptions(dictionary_list: list) -> None:
    correct_description_list = [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод организации",
        "Перевод организации",
    ]
    test_description_list = []
    test_description_list_part_two = []

    for elem in generators.transaction_descriptions(
        dictionary_list
    ):
        test_description_list.append(elem)

    for elem in generators.transaction_descriptions([]):
        test_description_list_part_two.append(elem)

    assert test_description_list == correct_description_list
    assert test_description_list_part_two == []


def test_card_number_generator() -> None:
    card_number = generators.card_number_generator(0, 4)
    assert next(card_number) == "0000 0000 0000 0000"
    assert next(card_number) == "0000 0000 0000 0001"
    assert next(card_number) == "0000 0000 0000 0002"
    assert next(card_number) == "0000 0000 0000 0003"
    assert next(card_number) == "0000 0000 0000 0004"
