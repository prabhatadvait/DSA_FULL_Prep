class Spreadsheet(object):

    def __init__(self, rows):
        self.mpp = {}   # store only explicitly set cells

    def setCell(self, cell, value):
        self.mpp[cell] = value   # assign value to cell

    def resetCell(self, cell):
        self.mpp[cell] = 0       # reset to 0 (default behavior)

    def getValue(self, formula):
        formula = formula[1:]    # strip leading '='
        for i in range(len(formula)):
            if formula[i] == '+':
                s1, s2 = formula[:i], formula[i+1:]
                
                # left operand: check if cell reference or integer
                left = self.mpp.get(s1, 0) if s1 and s1[0].isupper() else int(s1 or 0)
                
                # right operand: check if cell reference or integer
                right = self.mpp.get(s2, 0) if s2 and s2[0].isupper() else int(s2 or 0)
                
                return left + right
        
        return 0   # if no '+' in formula
