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
def inorder(root):
    if(root == 'No'):
        return 'No';
    if(root == None):
        return None;
    if(inorder(root.left) == 'No'):
        return 'No';
    orderOutput.append(root.key);
    if(orderOutput[-2] > orderOutput[-1]):
        return 'No';
    if(inorder(root.right) == 'No'):
        return 'No';
numNodes = int(input());
nodesTree = [Node() for i in range(numNodes)];
orderOutput = [-9999999999999];
def main():
    global orderOutput;
    for i in range(numNodes):
        key, left, right = map(int, input().split());
        nodesTree[i].setNode(key, nodesTree[left] if left != -1 else None, nodesTree[right] if right != -1 else None);
    if(numNodes == 0):
        print('CORRECT');
    else:
        result = inorder(nodesTree[0]);
        if(result == None or result != 'No'):
            print('CORRECT');
        else:
            print('INCORRECT');
threading.Thread(target=main).start()
