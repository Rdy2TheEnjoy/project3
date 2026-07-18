from typing import Any, Dict, List

import pytest

from src.widget import get_date, mask_account_card

# ---------- ТЕСТЫ ДЛЯ mask_account_card ----------

@pytest.mark.parametrize("input_info, expected", [
    ("Visa Platinum 1234567890123456", "Visa Platinum 1234 56** **** 3456"),
    ("MasterCard 1111222233334444", "MasterCard 1111 22** **** 4444"),
    ("МИР 0000000000000000", "МИР 0000 00** **** 0000"),
    ("Счет 1234567890", "Счет **7890"),
    ("Счет 9876543210", "Счет **3210"),
    ("счет 1111222233334444", "счет **4444"),
])
def test_mask_account_card_valid(input_info: str, expected: str) -> None:
    """Параметризованный тест маскировки карт и счетов"""
    assert mask_account_card(input_info) == expected


def test_mask_account_card_without_space() -> None:
    """Тест: если нет пробела, возвращается исходная строка"""
    input_info: str = "VisaPlatinum1234567890123456"
    result: str = mask_account_card(input_info)
    assert result == input_info


def test_mask_account_card_empty_string() -> None:
    """Тест: пустая строка"""
    result: str = mask_account_card("")
    assert result == ""


def test_mask_account_card_unknown_type() -> None:
    """Тест: неизвестный тип карты всё равно маскируется"""
    input_info: str = "UnknownCard 1234567890123456"
    result: str = mask_account_card(input_info)
    assert "****" in result


# ---------- ТЕСТЫ ДЛЯ get_date ----------

@pytest.mark.parametrize("iso_date, expected", [
    ("2023-05-20T15:30:00", "20.05.2023"),
    ("2023-01-01T00:00:00", "01.01.2023"),
    ("2024-12-31T23:59:59", "31.12.2024"),
    ("2023-03-15", "15.03.2023"),
    ("2023-03-15T10:00", "15.03.2023"),
])
def test_get_date_valid(iso_date: str, expected: str) -> None:
    """Параметризованный тест форматирования даты"""
    assert get_date(iso_date) == expected


def test_get_date_empty_string() -> None:
    """Тест: пустая строка вызывает ошибку"""
    with pytest.raises(ValueError):
        get_date("")


def test_get_date_with_timezone() -> None:
    """Тест с часовым поясом"""
    result: str = get_date("2023-06-10T12:00:00+03:00")
    assert result == "10.06.2023"
