from typing import List, Dict, Any, Union

def filter_by_state(list_dict: List[Dict[str, Any]], state: str = 'EXECUTED') -> List[Dict[str, Any]]:
    ''' Фильтрует список словарей по указанному значению ключа 'state''''
    new_list = []
    for item in list_dict:
        if item.get("state") == state:
            new_list.append(item)
    return new_list


def sort_by_date(list_dict: List[Dict[str, Any]], descending: bool = True) -> List[Dict[str, Any]]:
    ''' Сортирует список словарей по ключу 'date''''
    new_list = list_dict.copy()
    return sorted(new_list, key=lambda x: x["date"], reverse=descending)
