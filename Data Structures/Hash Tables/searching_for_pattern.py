# Source code in python3
def sumHash(string):
    return sum([ord(string[i]) for i in range(len(string))]);

def preComputeHashes():
    firstHash = sumHash(text[0:lenPattern]);
    preComputedHashes[0] = firstHash;
    for i in range(1, lenText-lenPattern+1):
        preComputedHashes[i] = preComputedHashes[i-1] - ord(text[i-1]) + ord(text[i+lenPattern-1]);

def findPattern():
    hashValueOfPattern = sumHash(pattern);
    foundPositions = [];
    preComputeHashes();
    for i in range(0, lenText-lenPattern+1):
        if(preComputedHashes[i] != hashValueOfPattern):
            continue;
        else:
            if(text[i:i+lenPattern] == pattern):
                foundPositions.append(i);
    return foundPositions;
pattern = input();
text = input();
lenPattern = len(pattern);
lenText = len(text); 
preComputedHashes = [None] * (lenText - lenPattern + 1);
print(*findPattern());