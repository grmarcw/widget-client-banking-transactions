import pytest

from scr import masks


@pytest.mark.parametrize(
    "number_card, result",
    [
        ("8912292571489222", "8912 29** **** 9222"),
        ("", "Номер карты состоит из 16 цифр."),
        ("5383", "Номер карты состоит из 16 цифр."),
        ("74937563849576385849", "Номер карты состоит из 16 цифр."),
        ("1234h67890123456", "Номер карты состоит только из цифр"),
    ],
)
def test_get_mask_card_number(number_card: str, result: str) -> None:
    assert masks.get_mask_card_number(number_card) == result


@pytest.mark.parametrize('account_number, result', [("73654108430135874305", "**4305"),
        ("", 'Номер счета состоит из 20 цифр'),
        ("5383", "Номер счета состоит из 20 цифр"),
        ("749375638495763858496", "Номер счета состоит из 20 цифр"),
        ("1234h678901234566365", "Номер счета может состоять только из цифр")])
def test_get_mask_account(account_number, result):
    assert masks.get_mask_account(account_number) == result
