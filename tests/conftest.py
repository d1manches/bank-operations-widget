import pytest
from typing import List, Dict, Any


@pytest.fixture
def transaction_data() -> List[Dict[str, Any]]:
    """Фикстура с тестовыми данными."""
    return [
        {"date": "2023-10-27T10:00:00.000Z", "state": "EXECUTED"},
        {"date": "2023-10-26T10:00:00.000Z", "state": "EXECUTED"},
        {"date": "2023-10-28T10:00:00.000Z", "state": "CANCELED"},
        {"date": "2023-10-27T12:00:00.000Z", "state": "EXECUTED"},
        {"date": "2023-10-27T10:00:00.000Z", "state": "PENDING"},
    ]


@pytest.fixture
def sample_transactions() -> List[Dict[str, Any]]:
    """Фикстура, списка транзакций."""
    return [
        {
            "id": 1,
            "operationAmount": {"currency": {"code": "USD"}},
            "description": "USD Transaction 1",
        },
        {
            "id": 2,
            "operationAmount": {"currency": {"code": "EUR"}},
            "description": "EUR Transaction 1",
        },
        {
            "id": 3,
            "operationAmount": {"currency": {"code": "USD"}},
            "description": "USD Transaction 2",
        },
    ]