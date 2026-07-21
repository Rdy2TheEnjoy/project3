

def filter_by_currency(transactions, currency_code):
    """Фильтрует транзакции по заданной валюте"""
    for i in transactions:
        if i["currency"] == currency_code:
            yield i


def transaction_descriptions(transactions):
    """Возвращает описание каждой транзакции"""
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start, stop):
    """Генерирует номера банковских карт в заданном диапазоне"""
    for number in range(start, stop + 1):
        card_str = f"{number:016d}"
        formatted = f"{card_str[:4]} {card_str[4:8]} {card_str[8:12]} {card_str[12:16]}"
        yield formatted
