from functools import wraps


def log(filename=None):
    """
    декоратор логирует в файл/консоль:
    начало работы функции
    результат функции/сообщение об ошибке
    завершение работы функции
    """
    def decorator(function):
        @wraps(function)
        def inner(*args, **kwargs):
            start = f"Начало работы функции {function.__name__}"
            finish = f"Работа функции {function.__name__} завершена"
            try:
                func = function(*args, **kwargs)
                result = f"Результат работы функции: {func}"
                if filename is not None:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(start + "\n")
                        file.write(result + "\n")
                        file.write(finish + "\n")
                else:
                    return f"{start}\n{result}\n{finish}"
            except Exception as e:
                if filename is not None:
                    error = f"ошибка: {e}"
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(start + "\n")
                        file.write(error + "\n")
                        file.write(finish + "\n")
                else:
                    return f"{start}\nошибка: {e}\n{finish}"

        return inner

    return decorator

