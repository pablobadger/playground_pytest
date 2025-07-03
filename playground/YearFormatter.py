from playground.Translator import Translator


class YearFormatter:
    def __init__(self, translator: Translator):
        self.translator = translator

    def format(self, year: int) -> str:
        translated_year = self.translator.translate(year)
        if translated_year is None:
            return "Invalid year. Please enter a year between 1 and 3999."
        return f"The year {year} in {self.translator.name} is: {translated_year}"
