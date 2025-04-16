import os

from scr.decorators import log


def test_log_without_file():
    @log()
    def example_func(x, y):
        return x / y

    example_1 = example_func(14, 0)
    example_2 = example_func(14, 2)

    start = "Начало работы функции example_func"
    result = "Результат работы функции: 7.0"
    error = "ошибка: division by zero"
    finish = "Работа функции example_func завершена"

    assert example_1 == f"{start}\n{error}\n{finish}"
    assert example_2 == f"{start}\n{result}\n{finish}"


def test_log_with_file():
    @log("my_log.txt")
    def example_func(x, y):
        return x / y

    example_func(14, 0)
    example_func(14, 2)

    start = "Начало работы функции example_func"
    result = "Результат работы функции: 7.0"
    error = "ошибка: division by zero"
    finish = "Работа функции example_func завершена"

    with open("my_log.txt", "r", encoding="utf-8") as file:
        file_ = file.read()

    assert (
        file_ == f"{start}\n{error}\n{finish}\n{start}\n{result}\n{finish}\n"
    )

    os.remove('my_log.txt')

