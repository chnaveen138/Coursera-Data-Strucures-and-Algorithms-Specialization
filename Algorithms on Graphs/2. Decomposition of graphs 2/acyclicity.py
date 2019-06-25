# Source code in python3
class Graph:
    def __init__(self):
        self.visited = dict();
        self.adjacencyList = dict();
        self.exploreTracker = dict();
    def exploreCyclicHelper(self, vertex):
        self.visited[vertex] = 1;
        self.exploreTracker[vertex] = 1;
        for neighbor in self.adjacencyList[vertex]:
            if(self.visited[neighbor] == 0):
                if(self.exploreCyclicHelper(neighbor)):
                    return True;
            elif(self.exploreTracker[neighbor] == 1):
                return True;
        self.exploreTracker[vertex] = 0;
        return False;
    def dfsCyclicHelper(self):
        vertices = self.visited.keys();
        for vertex in vertices:
            if(self.visited[vertex] == 0):
                if(self.exploreCyclicHelper(vertex)):
                    return True;
        return False;
    def containsCycle(self):
        return self.dfsCyclicHelper();

numNodes, numEdges = map(int, input().split());
graph = Graph();
for i in range(1, numNodes+1):
    graph.adjacencyList[i] = [];
for i in range(numEdges):
    vertex1, vertex2 = map(int, input().split());
    graph.adjacencyList[vertex1].append(vertex2);
for vertex in graph.adjacencyList.keys():
    graph.visited[vertex] = 0;
    graph.exploreTracker[vertex] = 0;
if(graph.containsCycle()):
    print(1);
else:
    print(0);