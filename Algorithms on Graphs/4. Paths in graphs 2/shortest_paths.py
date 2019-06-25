# Source code in python3
class Graph:
    def __init__(self, numNodes, numEdges):
        self.weights = dict();
        self.adjacencyList = dict();
        self.distances = dict();
        self.numNodes = numNodes;
        self.numEdges = numEdges;
        self.possibility = dict();
    def shortestDistances(self, source):
        reachability = dict();
        for vertex in range(1, self.numNodes+1):
            self.distances[vertex] = float('inf');
            self.possibility[vertex] = 1;
            reachability[vertex] = 0;
        reachability[source] = 1;
        self.distances[source] = 0;
        for i in range(self.numNodes-1):
            for edge in self.weights.keys():
                u = edge[0];
                v = edge[1];
                comparingWeight = self.distances[u] + self.weights[(u,v)];
                if(self.distances[v] > comparingWeight):
                    self.distances[v] = comparingWeight;
                    reachability[v] = 1;
        bfsQueue = [];
        for edge in self.weights.keys():
            u = edge[0];
            v = edge[1];
            comparingWeight = self.distances[u] + self.weights[(u,v)];
            if(self.distances[v] > comparingWeight):
                bfsQueue.append(v);
                self.possibility[v] = 0;
        while(bfsQueue):
            exploringVertex = bfsQueue.pop(0);
            for neighbor in self.adjacencyList[exploringVertex]:
                if(self.possibility[neighbor] == 1):
                    self.possibility[neighbor] = 0;
                    bfsQueue.append(neighbor);
        shortestDistances = [];
        for vertex in range(1, self.numNodes+1):
            if(reachability[vertex] == 0):
                shortestDistances.append('*');
            elif(self.possibility[vertex] == 0):
                shortestDistances.append('-');
            else:
                shortestDistances.append(self.distances[vertex]);
        return shortestDistances;

numNodes, numEdges = map(int, input().split());
graph = Graph(numNodes, numEdges);
for i in range(1, numNodes+1):
    graph.adjacencyList[i] = [];
for i in range(numEdges):
    vertex1, vertex2, weight = map(int, input().split());
    graph.adjacencyList[vertex1].append(vertex2);
    graph.weights[(vertex1, vertex2)] = weight;
source = int(input());
shortestDistances = graph.shortestDistances(source);
for distance in shortestDistances:
    print(distance);