import sys
import pytest
import json
sys.path.append("src")
from inkylayout import inky_layout

# content of test_sample.py
def func(x):
    return x + 1


def test_onerow_onecol_matchessnapshot(snapshot):
    layout = inky_layout(100,100)
    layout.add_row("row1")
    layout.add_col("row1",{"value":"testval1"})
    result = layout.render()
    snapshot.assert_match(json.dumps(result), 'snapshot.txt')

def test_onerow_threecols_numberrowscorrect():
    layout = inky_layout(90,100)
    layout.add_row("row1")
    layout.add_col("row1",{"value":"testval1"})
    layout.add_col("row1",{"value":"testval2"})
    layout.add_col("row1",{"value":"testval3"})
    result = layout.render()
    print(result)
    assert len(result['rows']) == 1
    assert len(result['rows'][0]['cols']) == 3
    assert result['rows'][0]['cols'][0]['width'] == 30

def test_towrow_numberrowscorrect():
    layout = inky_layout(90,100)
    layout.add_row("row1")
    layout.add_row("row2")
    layout.add_col("row1",{"value":"testval1"})
    layout.add_col("row1",{"value":"testval2"})
    layout.add_col("row2",{"value":"testval3"})
    result = layout.render()
    print(result)
    assert len(result['rows']) == 2
    assert len(result['rows'][0]['cols']) == 2
    assert len(result['rows'][1]['cols']) == 1
    