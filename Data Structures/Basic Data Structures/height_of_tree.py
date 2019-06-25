# Source code in python3
import sys, threading
sys.setrecursionlimit(10**7);
threading.stack_size(2**27);
class Node:
    def __init__(self):
        self.data = None;
        self.child = [];
    def addChild(self, node):
        self.child.append(node);
def getHeight(node):
    if(not node.child):
        return 1;
    else:
        return (1 + max(list(map(getHeight, node.child))));
def main():
    numberOfNodes = int(input());
    parentIndexes = list(map(int, input().split()));
    rootNode = Node();
    nodes = [Node() for i in range(0, numberOfNodes)]
    for childIndex in range(0, numberOfNodes):
        nodes[childIndex].data = childIndex;
        parentIndex = parentIndexes[childIndex];
        if(parentIndex == -1):
            rootNode = nodes[childIndex];
        else:
            nodes[parentIndex].addChild(nodes[childIndex]);
    print(getHeight(rootNode));
threading.Thread(target=main).start();

