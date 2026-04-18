def filter_by_state(list_dict, state='EXECUTED'):
    new_list = []
    for item in list_dict:
        if item.get('state') == state:
            new_list.append(item)
    return new_list


def sort_by_date(list_dict, descending=True):
    new_list = list_dict.copy()
    return sorted(new_list, key=lambda x: x['date'], reverse=descending)