# Source code in python3
listSize = int(input());
elementsList = list(map(int, input().split(" ")));
countsDict = dict();
for element in elementsList:
    if element in countsDict:
        countsDict[element] += 1;
    else:
        countsDict[element] = 1;
maxCount = countsDict[max(countsDict, key = countsDict.get)];
if(maxCount > int((listSize)/2)):
    print(1);
else:
    print(0);