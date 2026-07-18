from typing import Union


def get_mask_card_number(card_number: Union[int, str]) -> str:
    """Маскирует номер карты в формате XXXX XX** **** XXXX"""
    card_str = str(card_number)
    if not card_str.isdigit():
        raise ValueError("Номер карты должен содержать только цифры")
    if len(card_str) != 16:
        raise ValueError("Номер карты должен содержать 16 цифр")

    result = f"{card_str[:4]} {card_str[4:6]}** **** {card_str[-4:]}"
    return result


def get_mask_account(account_number: Union[int, str]) -> str:
    """маскирует номер счета"""
    account_str = str(account_number)

    if not account_str.isdigit():
        raise ValueError("Номер счета должен содержать только цифры")

    if len(account_str) < 4:
        raise ValueError("Номер счета должен содержать не менее 4 цифр")

    result = f"**{account_str[-4:]}"
    return result
