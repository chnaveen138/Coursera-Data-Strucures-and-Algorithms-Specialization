# Source code in python3
import pdb;
class Node:
    def __init__(self):
        self.key = None;
        self.left = None;
        self.right = None;
        self.parent = None;
    def setNode(self, key, left, right, parent):
        self.key = key;
        self.left = left;
        self.right = right;
        self.parent = parent;
def modValue(i):
    return ((i+lastSum) % m);
def leftDescendant(node):
    if(node.left == None):
        return node;
    return leftDescendant(node.left);
def rightAncestor(node):
    if(node.parent == None):
        return None;
    if(node.key < node.parent.key):
        return node.parent;
    return rightAncestor(node.parent);
def next(node):
    if(node.right != None):
        return leftDescendant(node.right);
    else:
        return rightAncestor(node);
def zig_zig(node, side):
    parent = node.parent;
    grandParent = parent.parent;
    if(side == 'll'):
        parent.left = parent.right;
        grandParent.left = node.right;
        node.right = parent;
        parent.right = grandParent;
    else:
        parent.right = parent.left;
        grandParent.right = node.left;
        node.left = parent;
        parent.left = grandParent;
    node.parent = grandParent.parent;
    parent.parent = node;
    grandParent.parent = parent;
def zig_zag(node, side):
    parent = node.parent;
    grandParent = parent.parent;
    if(side == 'lr'):
        parent.right = node.left;
        grandParent.left = node.right;
        node.left = parent;
        node.right = parent;
    else:
        parent.left = node.right;
        grandParent.right = node.left;
        node.right = parent;
        node.left = parent;
    node.parent = grandParent.parent;
    parent.parent = node;
    grandParent.parent = node;
def zig(node, side):
    parent = node.parent;
    if(side == 'l'):
        parent.left = node.right;
        node.right = parent;
    else:
        parent.right = node.left;
        node.left = parent;
    node.parent = parent.parent;
    parent.parent = node;
def splay(node):
    if(node == None or node.parent == None):
        return;
    parent = node.parent;
    grandParent = parent.parent if parent != None else None;
    if(grandParent == None):
        if(node.key < parent.key):
            zig(node, 'l');
        else:
            zig(node, 'r');
    elif(node.key < parent.key):
        if(parent.key < grandParent.key):
            zig_zig(node,'ll');
        else:
            zig_zag(node, 'rl');
    elif(node.key > parent.key):
        if(parent.key > grandParent.key):
            zig_zig(node,'rr');
        else:
            zig_zag(node, 'lr');
    if(node.parent != None):
        splay(parent);
        rootPointer = parent;
def find(key, root):
    if(root.key == key):
        return root;
    elif(root.key > key):
        if(root.left != None):
            return find(key, root.left);
        return root;
    else:
        if(root.right != None):
            return find(key, root.right);
        return root;
def splayFind(key, root):
    if(root == None):
        return 'Not found';
    node = find(key, root);
    splay(node);
    rootPointer = node;
    if(node.key == key):
        return 'Found';
    else:
        return 'Not found';
def deleteRoot(node):
    rightChild = node.right;
    rightChild.left = node.left;
    rightChild.parent = None;
def add(key, root):
    node = find(key, root);
    if(node.key == key):
        return;
    newNode = Node();
    newNode.setNode(key, None, None, node);
    if(node.key > key):
        node.left = newNode;
    else:
        node.right = newNode;
    splayFind(key, root);
def delete(key, root):
    if(root == None):
        return;
    node = find(key, root);
    if(node.key != key):
        return;
    nextNode = next(node);
    if(nextNode.left == None and nextNode.right == None):
        nextNode.parent = None;
    splay(nextNode);
    rootPointer = nextNode;
    splay(node);
    rootPointer = node;
    deleteRoot(node);
def rangeSum(l, r, root):
    global lastSum;
    sum = 0;
    if(root == None):
        return sum;
    node = find(l,root);
    while(node.key <= r):
        if(node.key >= l):
            sum += node.key;
        node = next(node);
        if(node == None):
            break;
    lastSum = sum;
    return sum;
lastSum = 0;
m = 1000000001;
rootPointer = None;
numOperations = int(input());
results = [];
for i in range(numOperations):
    query = input().split();
    symbol = query[0];
    number1 = modValue(int(query[1]));
    if(symbol == '?'):
        results.append(splayFind(number1, rootPointer));
    elif(symbol == '+'):
        if(rootPointer == None):
            rootPointer = Node();
            rootPointer.setNode(number1, None, None, None);
        else:
            add(number1, rootPointer);
    elif(symbol == '-'):
        delete(number1, rootPointer);
    else:
        number2 = modValue(int(query[2]));
        results.append(rangeSum(number1, number2, rootPointer));
for result in results:
    print(result);