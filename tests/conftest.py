from typing import Any, Dict, List

import pytest


@pytest.fixture
def sample_transactions() -> List[Dict[str, Any]]:
    """Фикстура с типовым списком транзакций для фильтрации"""
    return [
        {"id": 1, "state": "EXECUTED", "date": "2023-01-15T10:00:00"},
        {"id": 2, "state": "CANCELED", "date": "2023-02-20T14:30:00"},
        {"id": 3, "state": "EXECUTED", "date": "2023-03-10T09:15:00"},
        {"id": 4, "state": "PENDING", "date": "2023-04-05T16:45:00"},
    ]


@pytest.fixture
def unsorted_transactions() -> List[Dict[str, Any]]:
    """Фикстура с НЕОТСОРТИРОВАННЫМИ транзакциями для теста сортировки"""
    return [
        {"id": 1, "date": "2023-03-15T10:00:00"},  # 15 марта
        {"id": 2, "date": "2023-01-20T14:30:00"},  # 20 января
        {"id": 3, "date": "2023-02-10T09:15:00"},  # 10 февраля
    ]
