import sys
import os
import pytest
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from modules.parse.parsewrapper import calc_evaluation


@pytest.mark.parametrize("evaluation, result", [("2+2", 4.0),
                                                ("3*(2**2)", 12.0)])
def test_parser(evaluation, result):
    assert calc_evaluation(evaluation) == result
