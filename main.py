from src.external_api import convert_to_rubles

# Рубли
rub_tx = {"amount": 100, "currency": "RUB"}
print(convert_to_rubles(rub_tx))  # 100.0

# Доллары или евро
usd_tx = {"amount": 10, "currency": "USD"}
print(convert_to_rubles(usd_tx))  # None, если API не работает