import pytest


@pytest.fixture
def empty_string() -> str:
    return ""


@pytest.fixture
def many_digits() -> str:
    return '123456789012345678901'


@pytest.fixture
def few_digits() -> str:
    return '123456789012345'
