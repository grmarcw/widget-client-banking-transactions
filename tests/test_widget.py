import pytest

from scr import widget


@pytest.mark.parametrize(
    "number, result",
    [
        (
            "Visa Platinum 7000792289606361",
            "Visa Platinum 7000 79** **** 6361",
        ),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("", "Номер счета или карты не должен быть пустым"),
        ("Visa Platinum 70007922896063", "Номер карты состоит из 16 цифр."),
        ("Счет73654108430135874", "Номер счета состоит из 20 цифр"),
        ("Visa Platinum 64582745g8452046", "Номер карты состоит из 16 цифр."),
        ("счет283756092645r8426480", "Номер счета состоит из 20 цифр"),
    ],
)
def test_mask_account_card(number: str, result: str) -> None:
    assert widget.mask_account_card(number) == result


@pytest.mark.parametrize(
    "date, result",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("777357348", "Дата должна быть в формате 'iso'."),
    ],
)
def test_get_date(date: str, result: str) -> None:
    assert widget.get_date(date) == result
