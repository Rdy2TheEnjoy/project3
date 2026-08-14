import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.mark.parametrize("currency, expected_ids", [
    ("USD", [1, 3]),
    ("EUR", [2, 4]),
    ("RUB", [5]),
    ("GBP", []),
])
def test_filter_by_currency(transactions_data, currency, expected_ids):
    """Параметризованный тест фильтрации транзакций по валюте"""
    result = list(filter_by_currency(transactions_data, currency))
    result_ids = [t["id"] for t in result]
    assert result_ids == expected_ids


def test_filter_by_currency_empty_list(empty_transactions):
    """Тест фильтрации пустого списка транзакций"""
    result = list(filter_by_currency(empty_transactions, "USD"))
    assert result == []


def test_filter_by_currency_no_matches():
    """Тест фильтрации, когда нет транзакций с нужной валютой"""
    transactions = [
        {"id": 1, "amount": 100, "currency": "EUR", "description": "Перевод"},
        {"id": 2, "amount": 200, "currency": "EUR", "description": "Перевод"},
    ]
    result = list(filter_by_currency(transactions, "USD"))
    assert result == []


@pytest.mark.parametrize("transaction_list, expected", [
    ("transactions_data",
     ["Перевод организации", "Перевод со счета на счет", "Перевод с карты на карту",
      "Оплата услуг", "Пополнение счета"]),
    ("empty_transactions", []),
])
def test_transaction_descriptions(transaction_list, expected, request):
    """Параметризованный тест получения описаний транзакций"""
    transactions = request.getfixturevalue(transaction_list)
    result = list(transaction_descriptions(transactions))
    assert result == expected


def test_transaction_descriptions_single_transaction():
    """Тест с одной транзакцией"""
    transactions = [{"description": "Единственная транзакция"}]
    result = list(transaction_descriptions(transactions))
    assert result == ["Единственная транзакция"]


@pytest.mark.parametrize("start, end, expected", [
    (1, 5, [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
        "0000 0000 0000 0004",
        "0000 0000 0000 0005",
    ]),
    (1, 1, ["0000 0000 0000 0001"]),
    (0, 0, ["0000 0000 0000 0000"]),
    (9999999999999990, 9999999999999995, [
        "9999 9999 9999 9990",
        "9999 9999 9999 9991",
        "9999 9999 9999 9992",
        "9999 9999 9999 9993",
        "9999 9999 9999 9994",
        "9999 9999 9999 9995",
    ]),
])
def test_card_number_generator(start, end, expected):
    """Параметризованный тест генерации номеров карт"""
    result = list(card_number_generator(start, end))
    assert result == expected


@pytest.mark.parametrize("start, end, expected_count", [
    (10, 20, 11),
    (100, 105, 6),
    (0, 0, 1),
    (1, 100, 100),
])
def test_card_number_generator_count(start, end, expected_count):
    """Тест количества сгенерированных номеров"""
    result = list(card_number_generator(start, end))
    assert len(result) == expected_count


def test_card_number_generator_formatting():
    """Тест правильности форматирования"""
    result = list(card_number_generator(1, 1))
    assert result[0] == "0000 0000 0000 0001"
    assert len(result[0]) == 19
    blocks = result[0].split()
    for block in blocks:
        assert len(block) == 4
        assert block.isdigit()


def test_card_number_generator_edge_values():
    """Тест крайних значений диапазона"""
    result = list(card_number_generator(1, 1))
    assert result[0] == "0000 0000 0000 0001"

    result = list(card_number_generator(9999999999999999, 9999999999999999))
    assert result[0] == "9999 9999 9999 9999"
