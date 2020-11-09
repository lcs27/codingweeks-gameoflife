from generate_universe import *
from pytest import *


def test_generate_universe():
    assert generate_universe((4,4)) == [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]