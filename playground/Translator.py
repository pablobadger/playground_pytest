from abc import ABC


class Translator(ABC):
    def __init__(self):
        self.name = "Translator"

    def translate(self, number: int) -> str | None:
        raise NotImplementedError("Subclasses must implement this method.")
