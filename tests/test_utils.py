import pytest
import json
import os
from src.utils import load_transactions

def test_load_transactions_success(tmp_path):
    data = [{"id": 1, "amount": 100}]
    file_path = tmp_path / "operations.json"
    file_path.write_text(json.dumps(data), encoding="utf-8")

    result = load_transactions(str(file_path))
    assert result == data

def test_load_transactions_file_not_found():
    result = load_transactions("non_existent_file.json")
    assert result == []

def test_load_transactions_empty_file(tmp_path):
    file_path = tmp_path / "operations.json"
    file_path.write_text("", encoding="utf-8")

    result = load_transactions(str(file_path))
    assert result == []

def test_load_transactions_not_list(tmp_path):
    file_path = tmp_path / "operations.json"
    file_path.write_text(json.dumps({"key": "value"}), encoding="utf-8")

    result = load_transactions(str(file_path))
    assert result == []

def test_load_transactions_invalid_json(tmp_path):
    file_path = tmp_path / "operations.json"
    file_path.write_text("{ this is not json }", encoding="utf-8")

    result = load_transactions(str(file_path))
    assert result == []