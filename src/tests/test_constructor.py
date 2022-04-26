import sys
sys.path.append("src")
from inkylayout import inky_layout

def test_layoutconsturctor_initialiseslayout():
    layout = inky_layout(100,200)
    assert layout.layout == {"width":100, "height":200, "rows":[]}

