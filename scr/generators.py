from typing import Iterator


def filter_by_currency(dict_list: list, currency: str) -> Iterator[dict]:
    """
    создает новый список на основе старого,
    оставляя транзакции с нужной валютой
    возвращает элементы нового списка по одному
    """
    for transaction in dict_list:
        if transaction["operationAmount"]["currency"]["name"] == currency:
            yield transaction


def transaction_descriptions(dict_list: list) -> Iterator[str]:
    """
    выводит сообщения каждой транзакции по очереди
    """
    for transaction in dict_list:
        yield transaction["description"]


def card_number_generator(start: int, end: int) -> Iterator[str]:
    """
    генерирует номера карт
    :param start: с какого числа начать генерацию
    :param end: на каком числе завершить генерацию
    """
    for number in range(start, end + 1):
        # создаем номер карты с помощью форматирования(c_num = card_number)
        c_num = f"{number:016d}"

        yield f"{c_num[:4]} {c_num[4:8]} {c_num[8:12]} {c_num[12:]}"
