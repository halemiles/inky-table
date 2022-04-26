import sys
sys.path.append("src")
from inkylayout import InkyLayout

def test_layoutconsturctor_initialiseslayout():
    layout = InkyLayout(100,200)
    assert layout.layout == {"width":100, "height":200, "rows":[]}

