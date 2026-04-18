# Обработка банковских транзакций

## Цель проекта
Создание набора утилит для обработки банковских транзакций: маскировка карт и счетов, форматирование даты, фильтрация и сортировка транзакций.

## Модули и функции

### 1. masks.py - маскировка номеров

#### `get_mask_card_number(card_number: Union[int, str]) -> str`
Маскирует номер банковской карты.

**Пример:**
```python
>>> get_mask_card_number(1234567890123456)
'1234 56** **** 3456'
```
#### `get_mask_account(account_number: Union[int, str]) -> str`

Маскирует номер банковского счета.

**Пример:**
```python
>>> get_mask_account(12345678901234567890)
'**7890'
```
### 2. widget.py - форматирование данных

#### mask_account_card(card_or_account_info: str) -> str
Определяет тип (карта или счет) и маскирует номер.

**Пример:**
```python
>>> mask_account_card("Visa Platinum 1234567890123456")
'Visa Platinum 1234 56** **** 3456'

>>> mask_account_card("Счет 12345678901234567890")
'Счет **7890'
```
#### get_date(date_string: str) -> str
Преобразует дату из ISO формата в ДД.ММ.ГГГГ.

**Пример:**
```python
>>> get_date("2024-03-20T12:00:00")
'20.03.2024'
```
## 3. processing.py - Фильтрация и сортировка

### filter_by_state(list_dict, state='EXECUTED')

Фильтрует транзакции по статусу.

**Параметры:**
- `list_dict` - список словарей с транзакциями
- `state` - статус для фильтрации (по умолчанию 'EXECUTED')

**Пример:**
```python
>>> transactions = [
...     {'id': 1, 'state': 'EXECUTED'},
...     {'id': 2, 'state': 'PENDING'},
...     {'id': 3, 'state': 'EXECUTED'}
... ]
>>> filter_by_state(transactions)
[{'id': 1, 'state': 'EXECUTED'}, {'id': 3, 'state': 'EXECUTED'}]
```

### sort_by_date(list_dict, descending=True)

Сортирует транзакции по дате.

**Параметры:**
- `list_dict` - список словарей с транзакциями
- `descending` - True (новые сверху) или False (старые сверху)

**Пример:**
```python
>>> transactions = [
...     {'id': 1, 'date': '2024-01-15'},
...     {'id': 2, 'date': '2024-03-20'},
...     {'id': 3, 'date': '2024-02-10'}
... ]
>>> sort_by_date(transactions)
[{'id': 2, 'date': '2024-03-20'}, {'id': 3, 'date': '2024-02-10'}, {'id': 1, 'date': '2024-01-15'}]
```
## Установка

1. Скачайте файлы:
   - `masks.py`
   - `widget.py`
   - `processing.py`

2. Поместите их в одну папку

## Запуск и использование

```python
from masks import get_mask_card_number, get_mask_account
from widget import mask_account_card, get_date
from processing import filter_by_state, sort_by_date

# Пример работы с маскировкой
card_number = get_mask_card_number(1234567890123456)
account_number = get_mask_account(12345678901234567890)
print(card_number)
print(account_number)

# Пример работы с датой
date = get_date("2024-03-20T12:00:00")
print(date)

# Пример фильтрации и сортировки
transactions = [
    {'id': 1, 'state': 'EXECUTED', 'date': '2024-03-20'},
    {'id': 2, 'state': 'PENDING', 'date': '2024-01-15'},
    {'id': 3, 'state': 'EXECUTED', 'date': '2024-04-01'}
]

filtered = filter_by_state(transactions)
sorted_data = sort_by_date(filtered)
print(sorted_data)
```
## Зависимости

- Python 3.14 или выше
- Дополнительные библиотеки не требуются (используется только стандартная библиотека Python)
## Конфигурация

Проект не требует дополнительной конфигурации. Все функции работают сразу после копирования файлов.
## Автор

[[Rdy2TheEnjoy](https://github.com/Rdy2TheEnjoy)]
