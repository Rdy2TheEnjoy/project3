from typing import Union

import pytest

from src.masks import get_mask_account, get_mask_card_number

# ---------- ТЕСТЫ ДЛЯ get_mask_card_number ----------

@pytest.mark.parametrize("card_input, expected", [
    ("1234567890123456", "1234 56** **** 3456"),
    ("1111222233334444", "1111 22** **** 4444"),
    ("0000000000000000", "0000 00** **** 0000"),
    (1234567890123456, "1234 56** **** 3456"),
    (1111222233334444, "1111 22** **** 4444"),
])
def test_get_mask_card_number_valid(card_input: Union[int, str], expected: str) -> None:
    """Тест маскировки валидных номеров карт"""
    assert get_mask_card_number(card_input) == expected


@pytest.mark.parametrize("invalid_input", [
    "123456789012345",    # 15 цифр
    "12345678901234567",  # 17 цифр
    "1234",               # 4 цифры
])
def test_get_mask_card_number_invalid_length(invalid_input: str) -> None:
    """Тест с номерами неправильной длины"""
    with pytest.raises(ValueError, match="Номер карты должен содержать 16 цифр"):
        get_mask_card_number(invalid_input)


def test_get_mask_card_number_invalid_chars() -> None:
    """Тест с номером, содержащим буквы"""
    with pytest.raises(ValueError, match="Номер карты должен содержать только цифры"):
        get_mask_card_number("abcd1234efgh5678")


def test_get_mask_card_number_empty_string() -> None:
    """Тест с пустой строкой"""
    with pytest.raises(ValueError, match="Номер карты должен содержать только цифры"):
        get_mask_card_number("")


# ---------- ТЕСТЫ ДЛЯ get_mask_account ----------

@pytest.mark.parametrize("account_input, expected", [
    ("1234567890", "**7890"),
    ("1111", "**1111"),
    ("9876543210", "**3210"),
    (1234567890, "**7890"),
    (1111, "**1111"),
])
def test_get_mask_account_valid(account_input: Union[int, str], expected: str) -> None:
    """Тест маскировки валидных номеров счетов"""
    assert get_mask_account(account_input) == expected


@pytest.mark.parametrize("invalid_input", [
    "123",   # 3 цифры
    "1",     # 1 цифра
])
def test_get_mask_account_invalid_length(invalid_input: str) -> None:
    """Тест с номерами счетов неправильной длины"""
    with pytest.raises(ValueError, match="Номер счета должен содержать не менее 4 цифр"):
        get_mask_account(invalid_input)


def test_get_mask_account_invalid_chars() -> None:
    """Тест с номером счета, содержащим буквы"""
    with pytest.raises(ValueError, match="Номер счета должен содержать только цифры"):
        get_mask_account("abcd1234")


def test_get_mask_account_empty_string() -> None:
    """Тест с пустой строкой для счета"""
    with pytest.raises(ValueError, match="Номер счета должен содержать только цифры"):
        get_mask_account("")
