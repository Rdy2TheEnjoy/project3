import json
import os


def load_transactions(file_path):
    """Загружает транзакции из JSON-файла"""
    if not os.path.exists(file_path):
        return []

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return []
    if not isinstance(data, list):
        return []
    return data
