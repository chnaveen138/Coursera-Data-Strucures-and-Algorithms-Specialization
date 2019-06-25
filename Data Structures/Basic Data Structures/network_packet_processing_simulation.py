# Source code in python3
import pdb;
class Queue:
    def __init__(self, size):
        self.queue = [];
        self.size = size;
    def enqueue(self, item):
        if(self.size == len(self.queue)):
            return False;
        else:
            self.queue.append(item);
    def dequeue(self):
        return self.queue.pop(0);
size, numberOfPackets = tuple(map(int, input().split()));
packetsQueue = Queue(numberOfPackets);
for i in range(0, numberOfPackets):
    packetsQueue.enqueue(tuple(map(int, input().split())));
processingQueue = Queue(size);
processingTimes = [];
trackTime = -1;
secondsTime = 0;
finishingTimes = Queue(numberOfPackets);
timeIncrease = False;
while(True):
    if(len(packetsQueue.queue) <= 0):
        break;
    if(len(finishingTimes.queue) > 0 and secondsTime == finishingTimes.queue[0]):
        processingQueue.dequeue();
    arrivedPackets = [];
    for packet in packetsQueue.queue:
        if(packet[0] == secondsTime):
            arrivedPackets.append(packet);
        else:
            break;
    for i in range(len(arrivedPackets)):
        packetsQueue.dequeue();
    for packet in arrivedPackets:
        trackTime = secondsTime;
        if(processingQueue.enqueue(packet) == False):
            processingTimes.append(-1);
        else:
            if(trackTime == -1 or trackTime < secondsTime):
                trackTime = secondsTime;
            prevTrackTime = trackTime;
            processingTimes.append(trackTime);
            trackTime = trackTime + packet[1];
            if(prevTrackTime == trackTime):
                processingQueue.queue.pop(-1);
            else:
                secondsTime += packet[1];
                finishingTimes.enqueue(trackTime);
    secondsTime += 1;
for time in processingTimes:
    print(time);