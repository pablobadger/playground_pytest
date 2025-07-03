import pytest
from playground.CrazyNumerals import CrazyNumerals
from playground.YearFormatter import YearFormatter


@pytest.fixture
def formatter(translator):
    translator = CrazyNumerals()
    return YearFormatter(translator)
