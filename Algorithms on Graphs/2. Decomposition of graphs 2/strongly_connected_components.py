# Source code in python3
import sys, threading;
sys.setrecursionlimit(10**7);
threading.stack_size(2**27);
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
    
    def explore2(self, vertex):
        self.visited[vertex] = 1;
        for neighbor in self.adjacencyList[vertex]:
            if(self.visited[neighbor] == 0):
                self.explore(neighbor);
numNodes, numEdges = map(int, input().split());
graph = Graph();
reverseGraph = Graph();
def getNumSCC():
    numSCC = 0;
    orderVertices = reverseGraph.getOrder();
    for vertex in orderVertices:
        graph.visited[vertex] = 0;
    for vertex in orderVertices:
        if(graph.visited[vertex] == 0):
            graph.explore2(vertex);
            numSCC += 1;
    return numSCC;
def main():
    for i in range(1, numNodes+1):
        reverseGraph.adjacencyList[i] = [];
        graph.adjacencyList[i] = [];
    for i in range(numEdges):
        vertex1, vertex2 = map(int, input().split());
        graph.adjacencyList[vertex1].append(vertex2);
        reverseGraph.adjacencyList[vertex2].append(vertex1);
    for vertex in reverseGraph.adjacencyList.keys():
        reverseGraph.visited[vertex] = 0;
        reverseGraph.preVisitTimes[vertex] = 0;
        reverseGraph.postVisitTimes[vertex] = 0;
    print(getNumSCC());
threading.Thread(target=main).start();