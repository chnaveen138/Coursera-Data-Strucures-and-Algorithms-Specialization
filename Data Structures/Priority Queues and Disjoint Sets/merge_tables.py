# Source code in python3
class DisjointSet():
    def __init__(self, numTables, sizes):
        self.initialSize = numTables;
        self.parents = [None]*numTables;
        self.sizes = sizes;
        self.ranks = [None]*numTables;
        self.max = max(self.sizes);
        self.makeSet();
    def makeSet(self):
        for i in range(self.initialSize):
            self.parents[i] = i;
            self.ranks[i] = 1;
    def find(self, i):
        if(i != self.parents[i]):
            self.parents[i] = self.find(self.parents[i]);
        return self.parents[i];
    def merge(self, destination, source):
        destinationId = self.find(destination);
        sourceId = self.find(source);
        if(sourceId != destinationId):
            if(self.ranks[destinationId] > self.ranks[sourceId]):
                self.parents[sourceId] = destinationId;
                self.sizes[destinationId] += self.sizes[sourceId];
                self.sizes[sourceId] = 0;
                self.max = max(self.max, self.sizes[destinationId]);
            else:
                self.parents[destinationId] = sourceId;
                self.sizes[sourceId] += self.sizes[destinationId];
                self.sizes[destinationId] = 0;
                self.max = max(self.max, self.sizes[sourceId]);
                if(self.ranks[destinationId] == self.ranks[sourceId]):
                    self.ranks[sourceId] += 1;
        return self.max;

numTables, numMergeOps = map(int, input().split());
sizes = list(map(int, input().split()));
queries = [None]*numMergeOps;
for i in range(numMergeOps):
    queries[i] = tuple(map(int, input().split()));
disjointSet = DisjointSet(numTables, sizes);
for query in queries:
    print(disjointSet.merge(query[0]-1, query[1]-1));
