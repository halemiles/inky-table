#!/bin/python
import json

class InkyLayout():

    layout = {}
    def __init__(self, width, height):
        self.layout = {"width":width, "height":height, "rows":[]}

    def add_row(self, rowname):
        self.layout["rows"].append({"name":rowname, "cols":[]})

    def add_col(self, rowname, *cols):        
        rowindex = -1
        try:
            for row in range(len(self.layout['rows'])):
                if self.layout['rows'][row]['name'] == rowname:
                    rowindex = row
            for col in cols:
                self.layout['rows'][rowindex]['cols'].append(col)
        except:
            print("Please check that rows exist")

    def verify_definition(self):
        return False

    def render(self):
        items = {"width":self.layout['width'], "height":self.layout['height'], "rows":[]}
        max_width = self.layout['width']
        rows = self.layout['rows']
        appended_rows = []
        for row in range(len(rows)):
            y = int(12 * row)
            cols = rows[row]['cols']
            appended_cols = []
            col_width = max_width / len(cols)
            for col in range(len(cols)):
                colvalue = cols[col]['value']
                x = int(col_width * col)
                appended_cols.append({"value":colvalue,"width":col_width, "x":x, "y":y})
            appended_rows.append({"name":"test","cols":appended_cols})
        items['rows'] = appended_rows
        return  items
