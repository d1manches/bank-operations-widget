import pytest
from src.decorators import log
from typing import Any


def test_log_to_file_success(tmpdir: Any) -> None:
    log_file = tmpdir.join("test.log")

    @log(filename=str(log_file))
    def my_function(x: int, y: int) -> int:
        return x + y

    result = my_function(1, 2)
    assert result == 3

    with open(str(log_file), "r") as f:
        log_content = f.read()
        assert "my_function ok" in log_content
        assert "Result: 3" in log_content


def test_log_to_file_error(tmpdir: Any) -> None:
    log_file = tmpdir.join("test.log")

    @log(filename=str(log_file))
    def my_function(x: int, y: int) -> None:
        raise ValueError("Test error")

    with pytest.raises(ValueError) as excinfo:
        my_function(1, 2)
    assert "Test error" in str(excinfo.value)

    with open(str(log_file), "r") as f:
        log_content = f.read()
        assert "my_function error" in log_content
        assert "ValueError" in log_content
        assert "Inputs: (1, 2), {}" in log_content


def test_log_to_console_success(capsys: Any) -> None:
    @log()
    def my_function(x: int, y: int) -> int:
        return x + y

    result = my_function(3, 4)
    assert result == 7

    captured = capsys.readouterr()
    assert "my_function ok" in captured.err
    assert "Result: 7" in captured.err


def test_log_to_console_error(capsys: Any) -> None:
    @log()
    def my_function(x: int, y: int) -> None:
        raise TypeError("Console test error")

    with pytest.raises(TypeError) as excinfo:
        my_function(5, 6)
    assert "Console test error" in str(excinfo.value)

    captured = capsys.readouterr()
    assert "my_function error" in captured.err
    assert "TypeError" in captured.err
    assert "Inputs: (5, 6), {}" in captured.err


def test_log_no_filename_provided(capsys: Any) -> None:
    @log()
    def add(x: int, y: int) -> int:
        return x + y

    add(5, 3)
    captured = capsys.readouterr()
    assert "add ok" in captured.err


def test_log_kwargs(tmpdir: Any) -> None:
    log_file = tmpdir.join("test.log")

    @log(filename=str(log_file))
    def greet(name: str = "World") -> str:
        return f"Hello, {name}!"

    greet(name="Alice")

    with open(str(log_file), "r") as f:
        log_content = f.read()
        assert "greet ok" in log_content
        assert "Result: Hello, Alice!" in log_content