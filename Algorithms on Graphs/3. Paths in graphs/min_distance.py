# Source code in python3
class Queue():
    def __init__(self):
        self.queue = [];
        self.length = 0;
    def enqueue(self, item):
        self.queue.append(item);
        self.length += 1;
    def dequeue(self):
        self.length -= 1;
        return self.queue.pop(0);
class Graph:
    def __init__(self):
        self.distance = dict();
        self.adjacencyList = dict();
    def shortestDistance(self, source, destination):
        for vertex in graph.adjacencyList.keys():
            graph.distance[vertex] = -1;
        trackingQueue = Queue();
        self.distance[source] = 0;
        trackingQueue.enqueue(source);
        while(trackingQueue.length > 0):
            u = trackingQueue.dequeue();
            for neighbor in self.adjacencyList[u]:
                if(self.distance[neighbor] == -1):
                    trackingQueue.enqueue(neighbor);
                    self.distance[neighbor] = self.distance[u] + 1;
                if(neighbor == destination):
                    return self.distance[destination];
        return self.distance[destination];
numNodes, numEdges = map(int, input().split());
graph = Graph();
for i in range(1, numNodes+1):
    graph.adjacencyList[i] = [];
for i in range(numEdges):
    vertex1, vertex2 = map(int, input().split());
    graph.adjacencyList[vertex1].append(vertex2);
    graph.adjacencyList[vertex2].append(vertex1);
source, destination = map(int, input().split());
minDistance = graph.shortestDistance(source, destination);
print(minDistance);