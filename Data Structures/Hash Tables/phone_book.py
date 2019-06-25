# Source code in python3
import random;

class PhoneEntry:
    def __init__(self, number, name):
        self.number = number;
        self.name = name;
class HashTable():
    def __init__(self):
        self.p = 1000000007;
        self.a = random.randint(1, self.p-1);
        self.m = 2;
        self.b = random.randint(1, self.p-1);
        self.keys = 0;
        self.numToName = [[] for i in range(0, self.m)];

    def intHash(self, number):
        return ((((self.a*number) + self.b) % self.p)%self.m);
    
    def findEntry(self, queryNumber):
        hashValue = self.intHash(queryNumber);
        found = False;
        for entry in self.numToName[hashValue]:
            if(entry.number == queryNumber):
                found = True;
                return entry.name;
        if(not found):
            return 'not found';

    def reHash(self):
        self.m = 2*self.m;
        newNumToName = [[] for i in range(0, self.m)];
        for listOfEntries in self.numToName:
            for entry in listOfEntries:
                newNumToName[self.intHash(entry.number)].append(entry);
        self.numToName = newNumToName;

    def addEntry(self, queryNumber, queryName):
        intHashValue = self.intHash(queryNumber);
        if(self.findEntry(queryNumber) == 'not found'):
            if((self.keys/self.m) > 0.9):
                self.reHash();
                intHashValue = self.intHash(queryNumber);
            self.numToName[intHashValue].append(PhoneEntry(queryNumber, queryName));
            self.keys += 1;
        else:
            for entry in self.numToName[intHashValue]:
                if(entry.number == queryNumber):
                    entry.name = queryName;
                    break;
        return;

    def deleteEntry(self, queryNumber):
        intHashValue = self.intHash(queryNumber);
        if(len(self.numToName[intHashValue]) > 0):
            for index, entry in enumerate(self.numToName[intHashValue]):
                if(entry.number == queryNumber):
                    self.numToName[intHashValue].pop(index);
                    self.keys -= 1;
                    return;
        else:
            return;
numQueries = int(input());
hashTable = HashTable();
results = [];
for i in range(numQueries):
    query = input().split();
    queryNumber = int(query[1]);
    if(query[0] == 'find'):
        results.append(hashTable.findEntry(queryNumber));
    elif(query[0] == 'add'):
        queryName = query[2];
        hashTable.addEntry(queryNumber, queryName);
    else:
        hashTable.deleteEntry(queryNumber);
for result in results:
    print(result);
