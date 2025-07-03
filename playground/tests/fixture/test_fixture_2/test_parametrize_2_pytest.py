import pytest

scenarios = (
    (-1, None),
    (0, None),
    (4000, None),
    (1, "I"),
    (4, "IV"),
    (2025, "MMXXV"),
    (3999, "MMMCMXCIX"),
)


class TestRomanNumerals2:
    @pytest.mark.parametrize("input,expected_output", scenarios)
    def test_translation(self, translator, input, expected_output):
        result = translator.translate(input)
        assert result == expected_output
