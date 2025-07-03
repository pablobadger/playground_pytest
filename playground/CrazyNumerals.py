from playground.Translator import Translator


class CrazyNumerals(Translator):
    NUMERALS = {
        "₿": 1000,
        "£₿": 900,
        "€": 500,
        "£€": 400,
        "£": 100,
        "₵£": 90,
        "$": 50,
        "₵$": 40,
        "₵": 10,
        "₾10": 9,
        "đ": 5,
        "₾đ": 4,
        "₾": 1,
    }
    MIN_NUMBER = 1
    MAX_NUMBER = 3999

    def __init__(self):
        self.name = "Crazy numerals"

    def translate(self, number: int) -> str | None:
        if not self.MIN_NUMBER <= number <= self.MAX_NUMBER:
            return None

        result = ""
        for numeral, arabic in self.NUMERALS.items():
            while number >= arabic:
                result += numeral
                number -= arabic
        return result
