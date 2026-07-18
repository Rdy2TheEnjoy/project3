from typing import Any, Dict, List

import pytest

from src.processing import filter_by_state, sort_by_date

# ---------- ТЕСТЫ ДЛЯ filter_by_state ----------

@pytest.mark.parametrize("state, expected_ids", [
    ("EXECUTED", [1, 3]),
    ("CANCELED", [2]),
    ("PENDING", [4]),
])
def test_filter_by_state(
    sample_transactions: List[Dict[str, Any]],
    state: str,
    expected_ids: List[int]
) -> None:
    """Параметризованный тест фильтрации по различным состояниям"""
    result = filter_by_state(sample_transactions, state)
    result_ids = [item["id"] for item in result]
    assert result_ids == expected_ids


def test_filter_by_state_default(
    sample_transactions: List[Dict[str, Any]]
) -> None:
    """Тест фильтрации с параметром по умолчанию (EXECUTED)"""
    result = filter_by_state(sample_transactions)
    assert len(result) == 2
    assert all(item["state"] == "EXECUTED" for item in result)


def test_filter_by_state_empty_list() -> None:
    """Тест фильтрации пустого списка"""
    result = filter_by_state([])
    assert result == []


def test_filter_by_state_no_matches(
    sample_transactions: List[Dict[str, Any]]
) -> None:
    """Тест фильтрации, когда нет совпадений"""
    result = filter_by_state(sample_transactions, "COMPLETED")
    assert result == []


def test_filter_by_state_missing_state() -> None:
    """Тест фильтрации, когда у элемента нет ключа state"""
    transactions: List[Dict[str, Any]] = [
        {"id": 1, "state": "EXECUTED"},
        {"id": 2, "amount": 100},
    ]
    result = filter_by_state(transactions, "EXECUTED")
    assert result == [{"id": 1, "state": "EXECUTED"}]


# ---------- ТЕСТЫ ДЛЯ sort_by_date ----------

def test_sort_by_date_descending(
    unsorted_transactions: List[Dict[str, Any]]
) -> None:
    """Тест сортировки по убыванию"""
    result = sort_by_date(unsorted_transactions, True)
    dates = [item["date"] for item in result]
    assert dates == sorted(dates, reverse=True)


def test_sort_by_date_ascending(
    unsorted_transactions: List[Dict[str, Any]]
) -> None:
    """Тест сортировки по возрастанию"""
    result = sort_by_date(unsorted_transactions, False)
    dates = [item["date"] for item in result]
    assert dates == sorted(dates)


def test_sort_by_date_default(
    unsorted_transactions: List[Dict[str, Any]]
) -> None:
    """Тест сортировки с параметром по умолчанию (по убыванию)"""
    result = sort_by_date(unsorted_transactions)
    dates = [item["date"] for item in result]
    assert dates == sorted(dates, reverse=True)


def test_sort_by_date_does_not_mutate_original(
    unsorted_transactions: List[Dict[str, Any]]
) -> None:
    """Тест: сортировка не должна изменять исходный список"""
    original = unsorted_transactions.copy()
    sort_by_date(unsorted_transactions)
    assert unsorted_transactions == original


def test_sort_by_date_empty_list() -> None:
    """Тест сортировки пустого списка"""
    result = sort_by_date([])
    assert result == []


def test_sort_by_date_single_item() -> None:
    """Тест сортировки списка с одним элементом"""
    transactions: List[Dict[str, Any]] = [{"id": 1, "date": "2023-01-15T10:00:00"}]
    result = sort_by_date(transactions)
    assert result == transactions
