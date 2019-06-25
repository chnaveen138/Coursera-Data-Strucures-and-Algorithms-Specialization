# Source code in python3
class Thread():
    def __init__(self, index, time):
        self.index = index;
        self.time = time;
class Heap():
    def __init__(self, size):
        self.size = size;
        self.maxSize = 2*size + 2;
        self.array = [None] * self.maxSize;
    def parent(self, i):
        return int((i-1)/2);
    def leftChild(self, i):
        return 2*i + 1;
    def rightChild(self, i):
        return 2*i + 2;
    def swap(self, i, j):
        self.array[i], self.array[j] = self.array[j], self.array[i];
    def shiftUp(self, i):
        while(i > 1):
            pIdx = self.parent(i);
            if(self.compareThreads(self.array[i], self.array[pIdx])):
                self.swap(i, pIdx);
                i = pIdx;
            else:
                break;
    def shiftDown(self, i):
        minIndex = i;
        lcIdx = self.leftChild(i);
        if((lcIdx < self.size) and (self.compareThreads(self.array[lcIdx], self.array[minIndex]))):
            minIndex = lcIdx;
        rcIdx = self.rightChild(i);
        if((rcIdx < self.size) and (self.compareThreads(self.array[rcIdx], self.array[minIndex]))):
            minIndex = rcIdx;
        if(i != minIndex):
            self.swap(i, minIndex);
            self.shiftDown(minIndex);
    def buildHeap(self):
        for i in range(int((self.size - 1)/2), -1, -1):
            self.shiftDown(i);
    def changePriority(self, i, time):
        oldTime = self.array[i].time;
        self.array[i].time = time;
        if(time > oldTime):
            self.shiftDown(i);
        else:
            self.shiftUp(i);
    def compareThreads(self, thread1, thread2):
        if(thread1.time != thread2.time):
            return thread1.time < thread2.time;
        else:
            return thread1.index < thread2.index;
numThreads, numJobs = list(map(int, input().split()));
processingTimes = list(map(int, input().split()));
processingQueue = Heap(numThreads);
processingInfo = [None] * numJobs;
for i in range(numThreads):
    processingQueue.array[i] = Thread(i, 0);
processingQueue.buildHeap();
for j in range(numJobs):
    threadIndex = processingQueue.array[0].index;
    startTime = processingQueue.array[0].time;
    processingInfo[j] = (threadIndex, startTime);
    processingQueue.changePriority(0, startTime + processingTimes[j]);
for info in processingInfo:
    print(info[0], info[1]);