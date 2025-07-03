import pytest


INVALID_YEAR_MESSAGE = "Invalid year. Please enter a year between 1 and 3999."

scenarios = (
    (-1, INVALID_YEAR_MESSAGE),
    (0, INVALID_YEAR_MESSAGE),
    (4000, INVALID_YEAR_MESSAGE),
    (1, "The year 1 in Crazy numerals is: ₾"),
    (4, "The year 4 in Crazy numerals is: ₾đ"),
    (2025, "The year 2025 in Crazy numerals is: ₿₿₵₵đ"),
    (3999, "The year 3999 in Crazy numerals is: ₿₿₿£₿₵£₾10"),
)


class TestYearFormatterWithCrazyNumerals:
    @pytest.mark.parametrize("input,expected_output", scenarios)
    def test_formatter(self, formatter, input, expected_output):
        result = formatter.format(input)
        assert result == expected_output
