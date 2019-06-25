# Source code in python3
import sys, threading
sys.setrecursionlimit(10**6);
threading.stack_size(2**27);

class Node:
    def __init__(self):
        self.key = None;
        self.left = None;
        self.right = None;
    def setNode(self, key, left, right):
        self.key = key;
        self.left = left;
        self.right = right;
def preorder(root):
    if(root == None):
        return;
    orderOutput.append(root.key);
    preorder(root.left);
    preorder(root.right);
def inorder(root):
    if(root == None):
        return;
    inorder(root.left);
    orderOutput.append(root.key);
    inorder(root.right);
def postorder(root):
    if(root == None):
        return;
    postorder(root.left);
    postorder(root.right);
    orderOutput.append(root.key);
numNodes = int(input());
nodesTree = [Node() for i in range(numNodes)];
orderOutput = [];
def main():
    global orderOutput
    for i in range(numNodes):
        key, left, right = map(int, input().split());
        nodesTree[i].setNode(key, nodesTree[left] if left != -1 else None, nodesTree[right] if right != -1 else None);
    inorder(nodesTree[0]);
    print(*orderOutput);
    orderOutput = [];
    preorder(nodesTree[0]);
    print(*orderOutput);
    orderOutput = [];
    postorder(nodesTree[0]);
    print(*orderOutput);
threading.Thread(target=main).start()

