import os

from quantel import Quantel


def test_init():
    qt = Quantel(api_key=os.getenv("QUANTEL_API_KEY"))
    goog = qt.ticker('goog')

    assert goog.income_statement
