import pytest
from playground.RomanNumerals import RomanNumerals

scenarios = (
    (-1, None),
    (0, None),
    (4000, None),
    (1, "I"),
    (4, "IV"),
    (2025, "MMXXV"),
    (3999, "MMMCMXCIX"),
)


class TestRomanNumerals:
    @pytest.mark.parametrize("input,expected_output", scenarios)
    def test_translation(self, input, expected_output):
        translator = RomanNumerals()
        result = translator.translate(input)
        assert result == expected_output
