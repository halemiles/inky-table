import sys
import json
sys.path.append("src")
from inkylayout import InkyLayout

def test_onerow_onecol_matchessnapshot(snapshot):
    layout = InkyLayout(100,100)
    layout.add_row("row1")
    layout.add_col("row1",{"value":"testval1"})
    result = layout.render()
    snapshot.assert_match(json.dumps(result), 'snapshot.txt')

def test_onerow_threecols_numberrowscorrect(snapshot):
    layout = InkyLayout(90,100)
    layout.add_row("row1")
    layout.add_col("row1",{"value":"testval1"})
    layout.add_col("row1",{"value":"testval2"})
    layout.add_col("row1",{"value":"testval3"})
    result = layout.render()
    print(result)
    assert len(result['rows']) == 1
    assert len(result['rows'][0]['cols']) == 3
    assert result['rows'][0]['cols'][0]['x'] == 0
    assert result['rows'][0]['cols'][1]['x'] == 30
    assert result['rows'][0]['cols'][2]['x'] == 60
    
    assert result['rows'][0]['cols'][0]['y'] == 0
    assert result['rows'][0]['cols'][1]['y'] == 0
    assert result['rows'][0]['cols'][2]['y'] == 0
    snapshot.assert_match(json.dumps(result), 'snapshot.txt')

def test_tworows_numberrowscorrect():
    layout = InkyLayout(90,100)
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
    