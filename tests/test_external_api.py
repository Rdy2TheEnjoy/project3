from unittest.mock import patch

from src.external_api import convert_to_rubles


def test_convert_rub():
    transactions = {'amount': 100, 'currency': 'RUB'}
    assert convert_to_rubles(transactions) == 100.0


@patch('src.external_api.get_exchange_rate')
def test_convert_usd(mock_get_rate):
    mock_get_rate.return_value = 90.5
    transaction = {'amount': 10, 'currency': 'USD'}
    assert convert_to_rubles(transaction) == 905.0


@patch('src.external_api.get_exchange_rate')
def test_convert_api_error(mock_get_rate):
    mock_get_rate.return_value = None
    transaction = {'amount': 10, 'currency': 'USD'}
    assert convert_to_rubles(transaction) is None


@patch('src.external_api.get_exchange_rate')
def test_convert_eur(mock_get_rate):
    mock_get_rate.return_value = 85.0
    transaction = {'amount': 20, 'currency': 'EUR'}
    assert convert_to_rubles(transaction) == 1700.0
