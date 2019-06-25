# Source code in python3
class Graph:
    def __init__(self):
        self.visited = dict();
        self.adjacencyList = dict();
        self.numConnectedComponents = 1;
    def explore(self, vertex):
        self.visited[vertex] = self.numConnectedComponents;
        for neighbor in self.adjacencyList[vertex]:
            if(self.visited[neighbor] == 0):
                self.explore(neighbor);
    def dfsCheckComponents(self):
        vertices = self.visited.keys();
        for vertex in vertices:
            if(self.visited[vertex] == 0):
                self.explore(vertex);
                self.numConnectedComponents += 1;
        return self.numConnectedComponents-1;

numNodes, numEdges = map(int, input().split());
graph = Graph();
for i in range(1, numNodes+1):
    graph.adjacencyList[i] = [];
for i in range(numEdges):
    vertex1, vertex2 = map(int, input().split());
    graph.adjacencyList[vertex1].append(vertex2);
    graph.adjacencyList[vertex2].append(vertex1);
for vertex in graph.adjacencyList.keys():
    graph.visited[vertex] = 0;
print(graph.dfsCheckComponents());