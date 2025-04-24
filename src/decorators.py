from functools import wraps
import logging
from typing import Any, Callable, Optional, TypeVar, cast


T = TypeVar('T')
F = TypeVar('F', bound=Callable[..., Any])


def log(filename: Optional[str] = None) -> Callable[[F], F]:
    """
    Декоратор для логирования начала и конца выполнения функции, а также ее результатов или возникших ошибок.

    Args:
        filename (str, optional): Имя файла для записи логов. Если не указано, логи выводятся в консоль.

    Примеры:
        @log(filename="mylog.txt")
        def my_function(x: int, y: int) -> int:
            return x + y

        @log()
        def my_function_console(x: int, y: int) -> int:
            return x + y
    """

    def decorator(func: F) -> F:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            logger = logging.getLogger(func.__name__)
            logger.setLevel(logging.INFO)

            if filename:
                file_handler = logging.FileHandler(filename)
                formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
                file_handler.setFormatter(formatter)
                logger.addHandler(file_handler)
            else:
                stream_handler = logging.StreamHandler()
                formatter = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
                stream_handler.setFormatter(formatter)
                logger.addHandler(stream_handler)

            try:
                result = func(*args, **kwargs)
                logger.info(f"{func.__name__} ok - Result: {result}")
                return result
            except Exception as e:
                logger.error(f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}")
                raise  # Re-raise the exception to avoid masking errors

        return cast(F, wrapper)

    return decorator