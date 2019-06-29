# Source code in python3
from itertools import combinations;
class DisjointSet():
    def __init__(self, numVertices, sizes):
        self.initialSize = numVertices;
        self.parents = [None]*numVertices;
        self.sizes = sizes;
        self.ranks = [None]*numVertices;
        self.max = max(self.sizes);
        self.numSets = numVertices;
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
            self.numSets -= 1;
        return self.max;

def distance(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2)**(0.5);

numberOfPoints = int(input());
points = [];
sizes = [1 for i in range(numberOfPoints)];
pointIndexes = [i for i in range(numberOfPoints)];
edges = list(combinations(pointIndexes, 2));


for i in range(numberOfPoints):
    point = tuple(map(int, input().split()));
    points.append(point);
numClusters = int(input());

edges = sorted(edges, key = lambda k: distance(points[k[0]][0], points[k[0]][1], points[k[1]][0], points[k[1]][1]));
trackingSet = DisjointSet(numberOfPoints, sizes);

i = -1;
while(True):
    i += 1;
    if(trackingSet.find(edges[i][0]) != trackingSet.find(edges[i][1])):
        if(trackingSet.numSets == numClusters):
            break;
        trackingSet.merge(edges[i][0], edges[i][1]);
print(distance(points[edges[i][0]][0], points[edges[i][0]][1], points[edges[i][1]][0], points[edges[i][1]][1]));