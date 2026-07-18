from datetime import datetime
from typing import Any, Dict, List


def filter_by_state(list_dict: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """Фильтрует список словарей по указанному значению ключа state"""
    new_list = []
    for item in list_dict:
        if item.get("state") == state:
            new_list.append(item)
    return new_list


def sort_by_date(list_dict: List[Dict[str, Any]], descending: bool = True) -> List[Dict[str, Any]]:
    """Сортирует список словарей по ключу date"""
    new_list = list_dict.copy()

    def get_date(item: Dict[str, Any]) -> datetime:
        date_str = item["date"]
        date_part = date_str[:10]
        return datetime.strptime(date_part, "%Y-%m-%d")

    return sorted(new_list, key=get_date, reverse=descending)
