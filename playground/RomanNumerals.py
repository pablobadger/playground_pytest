from playground.Translator import Translator


class RomanNumerals(Translator):
    NUMERALS = {
        "M": 1000,
        "CM": 900,
        "D": 500,
        "CD": 400,
        "C": 100,
        "XC": 90,
        "L": 50,
        "XL": 40,
        "X": 10,
        "IX": 9,
        "V": 5,
        "IV": 4,
        "I": 1,
    }
    MIN_NUMBER = 1
    MAX_NUMBER = 3999

    def __init__(self):
        self.name = "Roman numerals"

    def translate(self, number: int) -> str | None:
        if not self.MIN_NUMBER <= number <= self.MAX_NUMBER:
            return None

        result = ""
        for numeral, arabic in self.NUMERALS.items():
            while number >= arabic:
                result += numeral
                number -= arabic
        return result
