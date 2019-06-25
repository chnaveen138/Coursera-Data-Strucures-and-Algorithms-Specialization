# Source code in python3
class Heap():
    def __init__(self, size):
        self.size = size;
        self.maxSize = 2*size + 2;
        self.array = [None] * self.maxSize;
        self.swaps = 0;
        self.swappedElements = [];
    def parent(self, i):
        return int((i-1)/2);
    def leftChild(self, i):
        return 2*i + 1;
    def rightChild(self, i):
        return 2*i + 2;
    def swap(self, i, j):
        temp = self.array[i];
        self.array[i] = self.array[j];
        self.array[j] = temp;
        self.swaps += 1;
        self.swappedElements.append((i, j));
    def shiftDown(self, i):
        minIndex = i;
        lcIdx = self.leftChild(i);
        if(lcIdx < self.size and self.array[minIndex] > self.array[lcIdx]):
            minIndex = lcIdx;
        rcIdx = self.rightChild(i);
        if(rcIdx < self.size and self.array[minIndex] > self.array[rcIdx]):
            minIndex = rcIdx;
        if(i != minIndex):
            self.swap(i, minIndex);
            self.shiftDown(minIndex);
    def buildHeap(self):
        for i in range(int((self.size - 1)/2), -1, -1):
            self.shiftDown(i);
numberOfElements = int(input());
heap = Heap(numberOfElements);
listOfElements = list(map(int, input().split()));
for i in range(numberOfElements):
    heap.array[i] = listOfElements[i];
heap.buildHeap();
print(heap.swaps);
for eachSwap in heap.swappedElements:
    print(eachSwap[0], eachSwap[1]);