import sys
import pytest
import json
sys.path.append("src")
from inkylayout import inky_layout

# content of test_sample.py
def func(x):
    return x + 1


def test_layoutconsturctor_initialiseslayout():
    layout = inky_layout(100,200)    
    assert layout.layout == {"width":100, "height":200, "rows":[]}

