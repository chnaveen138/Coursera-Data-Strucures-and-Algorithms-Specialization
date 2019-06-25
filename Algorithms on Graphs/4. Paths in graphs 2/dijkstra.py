# Source code in python3
import heapq;
class Graph:
    def __init__(self, numNodes, numEdges):
        self.weights = dict();
        self.adjacencyList = dict();
        self.distances = dict();
        self.numNodes = numNodes;
        self.numEdges = numEdges;

    def shortestDistance(self, source, destination):
        priorityQueue = [];
        length = 0;
        for vertexLabel in self.adjacencyList.keys():
            self.distances[vertexLabel] = float('inf');
            if(vertexLabel != source):
                heapq.heappush(priorityQueue, (float('inf'), vertexLabel));
                length += 1;
            else:
                heapq.heappush(priorityQueue, (0, vertexLabel));
                length += 1;
        relaxationTracker = set();
        self.distances[source] = 0;
        while(length > 0):
            relaxingVertex = heapq.heappop(priorityQueue)[1];
            length -= 1;
            if(relaxingVertex in relaxationTracker):
                continue;
            for neighbor in self.adjacencyList[relaxingVertex]:
                comparingWeight = self.distances[relaxingVertex] + self.weights[(relaxingVertex, neighbor)];
                if(self.distances[neighbor] > comparingWeight):
                    self.distances[neighbor] = comparingWeight;
                    heapq.heappush(priorityQueue, (self.distances[neighbor], neighbor));
                    length += 1;
            if(relaxingVertex == destination):
                if(self.distances[destination] == float('inf')):
                    return -1;
                return self.distances[destination];
            relaxationTracker.add(relaxingVertex);
        return -1;
numNodes, numEdges = map(int, input().split());
graph = Graph(numNodes, numEdges);
for i in range(1, numNodes+1):
    graph.adjacencyList[i] = [];
for i in range(numEdges):
    vertex1, vertex2, weight = map(int, input().split());
    graph.adjacencyList[vertex1].append(vertex2);
    graph.weights[(vertex1, vertex2)] = weight;
source, destination = map(int, input().split());
print(graph.shortestDistance(source, destination));