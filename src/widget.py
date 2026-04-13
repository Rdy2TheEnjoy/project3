from masks import get_mask_card_number, get_mask_account

def mask_account_card(card_or_account_info: str) -> str:
    parts = card_or_account_info.rsplit(' ', 1)
    if len(parts) != 2:
        return card_or_account_info
    card_type = parts[0]
    number = parts[1]
    if card_type.lower() == "счет":
        masked_number = get_mask_account(number)
        return f"{card_type} {masked_number}"
    else:
        masked_number = get_mask_card_number(number)
        return f"{card_type} {masked_number}"


def get_date(date_string: str) -> str:
    date_part = date_string[:10]
    year, month, day = date_part.split('-')
    return f"{day}.{month}.{year}"