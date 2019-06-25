# Source code in python3
import sys, threading
sys.setrecursionlimit(10**6);
from bisect import bisect
lengthList = 2;
lastSum = 0;
m = 1000000001;
def modValue(i):
    return ((i+lastSum) % m);
def add(key):
    global lengthList
    pos = bisect(sortedList, key);
    if(sortedList[pos-1] == key):
        return;
    else:
        sortedList.insert(pos, key);
        lengthList += 1;
def delete(key):
    global lengthList
    pos = bisect(sortedList, key);
    if(sortedList[pos-1] == key):
        sortedList.pop(pos-1);
        lengthList -= 1;
    else:
        return;
def find(key):
    pos = bisect(sortedList, key);
    if(sortedList[pos-1] == key):
        return "Found";
    else:
        return "Not found";
def rangeSum(l, r):
    global lastSum
    sum = 0;
    pos = bisect(sortedList, l);
    if(sortedList[pos-1] == l):
        sum += l;
    while (pos < lengthList) and sortedList[pos] <= r:
        if(sortedList[pos] >= l):
            sum += sortedList[pos];
        pos = pos+1;
    lastSum = sum;
    return sum;
sortedList = [-9999999999999,-99999999999];
numOperations = int(input());
results = [];
for i in range(numOperations):
    query = input().split();
    symbol = query[0];
    number1 = modValue(int(query[1]));
    if(symbol == '?'):
        results.append(find(number1));
    elif(symbol == '+'):
        add(number1);
    elif(symbol == '-'):
        delete(number1);
    else:
        number2 = modValue(int(query[2]));
        results.append(rangeSum(number1, number2));
for result in results:
    print(result);