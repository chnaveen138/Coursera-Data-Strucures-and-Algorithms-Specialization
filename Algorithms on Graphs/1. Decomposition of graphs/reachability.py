# Source code in python3
class Graph:
    def __init__(self):
        self.visited = dict();
        self.adjacencyList = dict();
    def explore(self, vertex):
        self.visited[vertex] = 1;
        for neighbor in self.adjacencyList[vertex]:
            if(not self.visited[neighbor]):
                self.explore(neighbor);
    def isTherePath(self, vertex1, vertex2):
        self.explore(vertex1);
        return self.visited[vertex2];
numNodes, numEdges = map(int, input().split());
graph = Graph();
for i in range(1, numNodes+1):
    graph.adjacencyList[i] = [];
for i in range(numEdges):
    vertex1, vertex2 = map(int, input().split());
    graph.adjacencyList[vertex1].append(vertex2);
    graph.adjacencyList[vertex2].append(vertex1);
source, destination = map(int, input().split());
for vertex in graph.adjacencyList.keys():
    graph.visited[vertex] = 0;
if(graph.isTherePath(source, destination)):
    print(1);
else:
    print(0);

