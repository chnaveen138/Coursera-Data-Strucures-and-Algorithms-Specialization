# Source code in python3
listSize = input();
elementsList = list(map(int, input().split(" ")));
def numberOfInversions(elementsList):
    appearances = dict();
    numberOfInversions = 0;
    for element in elementsList:
        if appearances.get(element) == None:
            appearances[element] = 1;
        for key in appearances:
            if element < key:
                numberOfInversions += appearances[key];
    return numberOfInversions;
print(numberOfInversions(elementsList));