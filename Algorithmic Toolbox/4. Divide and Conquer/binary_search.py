# Source code in python3
numbersList = list(map(int, input().split(" ")));
listSize = numbersList[0];
numbersList = numbersList[1:];
searchList = list(map(int, input().split(" ")));
searchListSize = searchList[0];
searchList = searchList[1:];

def binarySearch(key, low, high):
    if(high >= low):
        mid = round(low + (high - low)/2);
        if(numbersList[mid] == key):
            return mid;
        elif(numbersList[mid] > key):
            return binarySearch(key, low, mid - 1);
        else:
            return binarySearch(key, mid + 1, high);
    else:
        return -1;
keyIndexes = [binarySearch(key, 0, listSize - 1) for key in searchList];
print(*keyIndexes)
    
