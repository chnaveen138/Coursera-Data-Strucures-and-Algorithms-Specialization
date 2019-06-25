# Below source code in python3
size = int(input());
elements = list(map(int, input().split()));
firstMax = -9999999999999;
secondMax = -9999999999999;
firstMaxIndex = 0;
for index, element in enumerate(elements):
    if(elements[index] > firstMax):
        secondMax = firstMax;
        firstMax = elements[index];
        firstMaxIndex = index;
    if(elements[index] > secondMax and index != firstMaxIndex):
        secondMax = elements[index];
print(firstMax * secondMax);