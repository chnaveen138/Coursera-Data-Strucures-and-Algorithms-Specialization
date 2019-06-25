# Source code in python3
class Queue():
    def __init__(self):
        self.queue = [];
    def enqueue(self, item):
        self.queue.append(item);
    def dequeue(self):
        return self.queue.pop();
class Graph:
    def __init__(self):
        self.color = dict();
        self.adjacencyList = dict();
        self.numEdges = None;
    def isBipartite(self):
        trackingQueue = Queue();
        source = 1;
        self.color[source] = 1;
        trackingQueue.enqueue(source);
        while(trackingQueue.queue):
            u = trackingQueue.dequeue();
            for neighbor in self.adjacencyList[u]:
                if(self.color[neighbor] == -1):
                    self.color[neighbor] = 1 - self.color[u];
                    trackingQueue.enqueue(neighbor);
                elif(self.color[neighbor] == self.color[u]):
                    return False;
        return True;
numNodes, numEdges = map(int, input().split());
graph = Graph();
for i in range(1, numNodes+1):
    graph.adjacencyList[i] = [];
for i in range(numEdges):
    vertex1, vertex2 = map(int, input().split());
    graph.adjacencyList[vertex1].append(vertex2);
    graph.adjacencyList[vertex2].append(vertex1);
for vertex in graph.adjacencyList.keys():
    graph.color[vertex] = -1;
if(graph.isBipartite()):
    print(1);
else:
    print(0);
