import unittest

from playground.RomanNumerals import RomanNumerals
from playground.YearFormatter import YearFormatter


class TestYearFormatter(unittest.TestCase):
    INVALID_YEAR_MESSAGE = "Invalid year. Please enter a year between 1 and 3999."

    def test_given_a_negative_number_when_translating_then_none_returned(self):
        formatter = self._build_formatter()
        result = formatter.format(-1)
        assert result == self.INVALID_YEAR_MESSAGE

    def test_given_a_zero_number_when_translating_then_none_returned(self):
        formatter = self._build_formatter()
        result = formatter.format(0)
        assert result == self.INVALID_YEAR_MESSAGE

    def test_given_a_number_over_3999_when_translating_then_none_returned(self):
        formatter = self._build_formatter()
        result = formatter.format(4000)
        assert result == self.INVALID_YEAR_MESSAGE

    def test_given_2025_when_translating_then_MMXXV_returned(self):
        formatter = self._build_formatter()
        result = formatter.format(2025)
        assert result == "The year 2025 in Roman numerals is: MMXXV"

    def test_given_a_3999_when_translating_then_MMMCMXCIX_returned(self):
        formatter = self._build_formatter()
        result = formatter.format(3999)
        assert result == "The year 3999 in Roman numerals is: MMMCMXCIX"

    def _build_formatter(self) -> YearFormatter:
        translator = RomanNumerals()
        return YearFormatter(translator)
