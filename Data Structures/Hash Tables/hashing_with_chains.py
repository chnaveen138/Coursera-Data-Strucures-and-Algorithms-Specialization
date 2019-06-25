# Source code in python3
import random;

class Entry:
    def __init__(self, text):
        self.text = text;
class HashTable():
    def __init__(self, m):
        self.p = 1000000007;
        self.m = m;
        self.entriesList = [[] for i in range(0, self.m)];
        self.x = 263;

    def polyHash(self, string):
        hashValue = 0;
        for i in range(len(string)-1, -1, -1):
            hashValue = ((hashValue * self.x) + ord(string[i])) % self.p;
        return hashValue % self.m;

    def findEntry(self, queryText):
        hashValue = self.polyHash(queryText);
        found = False;
        for entry in self.entriesList[hashValue]:
            if(entry.text == queryText):
                found = True;
                return 'yes';
        if(not found):
            return 'no';

    def addEntry(self, queryText):
        hashValue = self.polyHash(queryText);
        if(self.findEntry(queryText) != 'yes'):
            self.entriesList[hashValue].insert(0, Entry(queryText));
        else:
            return;

    def deleteEntry(self, queryText):
        hashValue = self.polyHash(queryText);
        if(len(self.entriesList[hashValue]) > 0):
            for index, entry in enumerate(self.entriesList[hashValue]):
                if(entry.text == queryText):
                    self.entriesList[hashValue].pop(index);
                    return;
        else:
            return;

    def checkBucket(self, index):
        entryText = [];
        for entry in self.entriesList[index]:
            entryText.append(entry.text);
        return entryText;

m = int(input());
hashTable = HashTable(m);
numQueries = int(input());
results = [];
for i in range(numQueries):
    query = input().split();
    queryText = query[1];
    if(query[0] == 'find'):
        results.append(hashTable.findEntry(queryText));
    elif(query[0] == 'check'):
        results.append(hashTable.checkBucket(int(queryText)));
    elif(query[0] == 'add'):
        hashTable.addEntry(queryText);
    else:
        hashTable.deleteEntry(queryText);
for result in results:
    if(isinstance(result, str)):
        print(result);
    else:
        print(*result);