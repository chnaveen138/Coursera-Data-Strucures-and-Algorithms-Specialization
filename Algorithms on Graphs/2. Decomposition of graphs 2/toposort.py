# Source code in python3
class Graph:
    def __init__(self):
        self.visited = dict();
        self.adjacencyList = dict();
        self.preVisitTimes = dict();
        self.postVisitTimes = dict();
        self.timeTracker = 0;
    def preVisit(self, vertex):
        self.timeTracker += 1;
        self.preVisitTimes[vertex] = self.timeTracker;
    def postVisit(self, vertex):
        self.timeTracker += 1;
        self.postVisitTimes[vertex] = self.timeTracker;
    def explore(self, vertex):
        self.visited[vertex] = 1;
        self.preVisit(vertex);
        for neighbor in self.adjacencyList[vertex]:
            if(self.visited[neighbor] == 0):
                self.explore(neighbor);
        self.postVisit(vertex);
    def dfs(self):
        vertices = self.visited.keys();
        for vertex in vertices:
            if(self.visited[vertex] == 0):
                self.explore(vertex);
    def getOrder(self):
        self.dfs();
        return sorted(self.postVisitTimes, key = self.postVisitTimes.get, reverse = True);

numNodes, numEdges = map(int, input().split());
graph = Graph();
for i in range(1, numNodes+1):
    graph.adjacencyList[i] = [];
for i in range(numEdges):
    vertex1, vertex2 = map(int, input().split());
    graph.adjacencyList[vertex1].append(vertex2);
for vertex in graph.adjacencyList.keys():
    graph.visited[vertex] = 0;
    graph.preVisitTimes[vertex] = 0;
    graph.postVisitTimes[vertex] = 0;
print(*graph.getOrder());
