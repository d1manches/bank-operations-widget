import pytest
from typing import Optional
from src.widget import mask_account_card, get_date


class TestWidget:
    @pytest.mark.parametrize(
        "input_string, expected_mask",
        [
            ("Visa 1234567890123456", "Visa 1234 **** **** 3456"),
            ("Visa Platinum 7000792289606361", "Visa Plat **** **** 6361"),
            ("Счет 12345678901234567890", "Счет ****7890"),
            ("MasterCard 1234567890", "MasterCard 1234567890"),
            ("Счет 123", "Счет 123"),
            ("Invalid Input", "Invalid Input"),
            ("", ""),
            # Убрали тест с None, так как функция не принимает Optional[str]
        ],
    )
    def test_mask_account_card(self, input_string: str, expected_mask: str) -> None:
        assert mask_account_card(input_string) == expected_mask

    @pytest.mark.parametrize(
        "date_string, expected_date",
        [
            ("2023-10-26T10:00:00.000Z", "26.10.2023"),
            ("2023-1-1", "01.01.2023"),
            ("2023-10-26", "26.10.2023"),
            ("", None),
            (None, None),
        ],
    )
    def test_get_data(self, date_string: Optional[str], expected_date: Optional[str]) -> None:
        assert get_date(date_string) == expected_date