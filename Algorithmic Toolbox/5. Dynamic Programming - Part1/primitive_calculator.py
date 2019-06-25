# Source code in python3
def minOperationsAndNumbers(number, denominations):
    minOperationsUptoN = dict();
    minOperationsUptoN[1] = 0;
    intermediateNumbers = dict();
    intermediateNumbers[1] = 1;
    for n in range(2, number + 1):
        minOperationsUptoN[n] = 999999999999999;
        for j in denominations:
            if n >= j:
                if j == 1:
                    operations = minOperationsUptoN[n - j] + 1;
                elif((n/j).is_integer()):
                    operations = minOperationsUptoN[int(n/j)] + 1;
                if operations < minOperationsUptoN[n]:
                    minOperationsUptoN[n] = operations;
                    if j == 1:
                        intermediateNumbers[n] = n-1;
                    elif((n/j).is_integer()):
                        intermediateNumbers[n] = int(n/j);
    n = number;
    listOfIntermediateNumbersForN = [n];
    if(n == 1):
        listOfIntermediateNumbersForN = [n];
    else:
        while True:
            n = intermediateNumbers[n];
            listOfIntermediateNumbersForN.append(n);
            if n == 1:
                break;
    return [minOperationsUptoN[number], listOfIntermediateNumbersForN];
number = int(input());
denominations = [1, 2, 3];
minOperationsForN, intermediateNumbersForN = minOperationsAndNumbers(number, denominations);
print(minOperationsForN);
print(*intermediateNumbersForN[::-1]);