import unittest

from playground.RomanNumerals import RomanNumerals


class TestRomanNumerals(unittest.TestCase):
    def test_given_a_negative_number_when_translating_then_none_returned(self):
        translator = RomanNumerals()
        result = translator.translate(-1)
        assert result is None

    def test_given_a_zero_number_when_translating_then_none_returned(self):
        translator = RomanNumerals()
        result = translator.translate(0)
        assert result is None

    def test_given_a_number_over_3999_when_translating_then_none_returned(self):
        translator = RomanNumerals()
        result = translator.translate(4000)
        assert result is None

    def test_given_1_when_translating_then_I_returned(self):
        translator = RomanNumerals()
        result = translator.translate(1)
        assert result == "I"

    def test_given_4_when_translating_then_IV_returned(self):
        translator = RomanNumerals()
        result = translator.translate(4)
        assert result == "IV"

    def test_given_2025_when_translating_then_IV_returned(self):
        translator = RomanNumerals()
        result = translator.translate(2025)
        assert result == "MMXXV"

    def test_given_3999_when_translating_then_MMMCMXCIX_returned(self):
        translator = RomanNumerals()
        result = translator.translate(3999)
        assert result == "MMMCMXCIX"
