# Source code in python3
arithmeticExpression = list(input());
opfncs = {'+': lambda x, y: x + y,\
          '-': lambda x, y: x - y,\
          '*': lambda x, y: x * y}

def findMinAndMax(i, j):
    maxValue = -9999999999999999;
    minValue = +9999999999999999;
    for k in range(i, j):
        value1 = opfncs[operators[k]](maxValuesOfSubExps[i][k], maxValuesOfSubExps[k+1][j]);
        value2 = opfncs[operators[k]](maxValuesOfSubExps[i][k], minValuesOfSubExps[k+1][j]);
        value3 = opfncs[operators[k]](minValuesOfSubExps[i][k], maxValuesOfSubExps[k+1][j]);
        value4 = opfncs[operators[k]](minValuesOfSubExps[i][k], minValuesOfSubExps[k+1][j]);
        minValue = min(minValue, value1, value2, value3, value4);
        maxValue = max(maxValue, value1, value2, value3, value4);
    return [minValue, maxValue];

def virtualParenthesis():
    for i in range(size):
        minValuesOfSubExps[i][i] = integers[i];
        maxValuesOfSubExps[i][i] = integers[i];
    for k in range(1, size):
        for i in range((size - k)):
            j = i + k;
            minAndMaxValues = findMinAndMax(i, j);
            minValuesOfSubExps[i][j] = minAndMaxValues[0];
            maxValuesOfSubExps[i][j] = minAndMaxValues[1];
    return maxValuesOfSubExps[0][size-1];

integers = [];
operators = [];
for char in arithmeticExpression:
    if char in ['+',  '-', '*']:
        operators.append(char);
    else:
        integers.append(int(char));
size = len(integers);
maxValuesOfSubExps = [[0 for j in range(size)] for i in range(size)];
minValuesOfSubExps = [[0 for j in range(size)] for i in range(size)];
print(virtualParenthesis());