import pytest
from playground.RomanNumerals import RomanNumerals
from playground.YearFormatter import YearFormatter


@pytest.fixture
def translator():
    return RomanNumerals()
