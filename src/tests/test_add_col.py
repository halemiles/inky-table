import sys
sys.path.append("src")
from inkylayout import inky_layout

# content of test_sample.py
def func(x):
    return x + 1


def test_addrow_creates_newrow():
    layout = inky_layout(100,200)   
    layout.add_col("testrow1", {"value": "value1"}) 
    pass #Exceptions should be handled
