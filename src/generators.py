transactions = [
    {"id": 1, "amount": 100, "currency": "USD", "description": "Перевод организации"},
    {"id": 2, "amount": 200, "currency": "EUR", "description": "Перевод со счета на счет"},
    {"id": 3, "amount": 150, "currency": "USD", "description": "Перевод с карты на карту"},
    # ...
]

def filter_by_currency(transactions, currency_code):
    for i in transactions:
        if i["currency"] == currency_code:
            yield i

def transaction_descriptions(transactions):
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start, end):
    for number in range(start, end + 1):
        card_str = f"{number:016d}"
        formatted = f"{card_str[:4]} {card_str[4:8]} {card_str[8:12]} {card_str[12:16]}"
        yield formatted
