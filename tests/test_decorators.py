import pytest

from src.decorators import log


def test_log_success(capsys):
    """Проверяет, что декоратор выводит сообщение об успехе в консоль"""

    @log()
    def add(a, b):
        return a + b

    add(2, 3)

    captured = capsys.readouterr()
    assert "add ok" in captured.out


def test_log_error(capsys):
    """Проверяет, что декоратор выводит сообщение об ошибке в консоль"""

    @log()
    def divide(a, b):
        return a / b

    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

    captured = capsys.readouterr()
    assert "divide error" in captured.out


def test_log_to_file_success(tmp_path):
    """Проверяет, что декоратор записывает лог успеха в файл"""

    log_file = tmp_path / "test.log"
    filename = str(log_file)

    @log(filename=filename)
    def add(a, b):
        return a + b

    add(2, 3)

    assert log_file.read_text() == "add ok\n"


def test_log_to_file_error(tmp_path):
    """Проверяет, что декоратор записывает лог ошибки в файл"""

    log_file = tmp_path / "test.log"
    filename = str(log_file)

    @log(filename=filename)
    def divide(a, b):
        return a / b

    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

    content = log_file.read_text()
    assert "divide error" in content
    assert "division by zero" in content
