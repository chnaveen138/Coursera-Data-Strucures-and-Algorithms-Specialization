# Source code in python3
import queue

def getDistance(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2)**(0.5);

def maxConnectingDistance(points):
    minDistances = [float('inf')] * numberOfPoints;
    trackingQueue = queue.PriorityQueue();
    minDistances[0] = 0;
    minDistanceValue = 0;
    trackingQueue.put((0, 0));
    processedPoints = set();
    while(not trackingQueue.empty()):
        foundDistance, exploringPoint = trackingQueue.get();
        if(exploringPoint not in processedPoints):
            minDistanceValue += foundDistance;
            processedPoints.add(exploringPoint);
            for i in range(numberOfPoints):
                if(i not in processedPoints):
                    currentDistance = getDistance(points[i][0],  points[i][1], points[exploringPoint][0], points[exploringPoint][1]);
                    if(minDistances[i] > currentDistance):
                        minDistances[i] = currentDistance;
                        trackingQueue.put((currentDistance, i));
    return minDistanceValue;

numberOfPoints = int(input());
points = [];
sizes = [1 for i in range(numberOfPoints)];

for i in range(numberOfPoints):
    point = tuple(map(int, input().split())) + (i,);
    points.append(point);

print(maxConnectingDistance(points));