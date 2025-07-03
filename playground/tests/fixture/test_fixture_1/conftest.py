import pytest
from playground.RomanNumerals import RomanNumerals
from playground.YearFormatter import YearFormatter


@pytest.fixture
def formatter(translator):
    translator = RomanNumerals()
    return YearFormatter(translator)
