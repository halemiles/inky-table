#!/bin/python

class InkyLayout():
    """
    InkyLayout class to generate a JSON string 
    containing x/y co-ords and values to be consumed by the InkyPHAT framework
    """
    layout = {}
    def __init__(self, width, height):
        self.layout = {"width":width, "height":height, "rows":[]}

    def add_row(self, rowname):
        """Add a row including rowname. Must be added in order to create columns"""
        self.layout["rows"].append({"name":rowname, "cols":[]})

    def add_col(self, rowname, *cols):
        """ Add a column to an existing row"""
        rowindex = -1
        try:
            for row in range(len(self.layout['rows'])):
                if self.layout['rows'][row]['name'] == rowname:
                    rowindex = row
            for col in cols:
                self.layout['rows'][rowindex]['cols'].append(col)
        except:
            print("Please check that rows exist")

    def render(self):
        """Generate a JSON object for use with InkyPHAT"""
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
