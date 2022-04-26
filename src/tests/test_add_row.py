import sys
sys.path.append("src")
from inkylayout import inky_layout

# content of test_sample.py
def func(x):
    return x + 1


def test_addrow_creates_newrow():
    layout = inky_layout(100,200)
    layout.add_row("testrow1")
    assert layout.layout == {"width":100, "height":200,
        "rows":[{"name": "testrow1", "cols":[]}]
        }

def test_addtworow_creates_newtworows():
    layout = inky_layout(100,200)
    layout.add_row("testrow1")
    layout.add_row("testrow2")
    assert layout.layout == {"width":100, "height":200, 
        "rows":[{"name": "testrow1", "cols":[]},{"name": "testrow2", "cols":[]}]
        }
