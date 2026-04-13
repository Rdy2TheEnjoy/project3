from typing import Union


def get_mask_card_number(card_number: Union[int, str]) -> str:
    """маскирует номер карты."""
    card_str = str(card_number)
    result = f"{card_str[:4]} {card_str[4:6]}** **** {card_str[-4:]}"
    return result


def get_mask_account(account_number: Union[int, str]) -> str:
    """маскирует номер счета"""
    account_str = str(account_number)
    result = f"**{account_str[-4:]}"
    return result
