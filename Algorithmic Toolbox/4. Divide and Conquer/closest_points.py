# Source code in python3
def distance(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2)**(0.5);

numberOfPoints = int(input());
points = [];

for i in range(numberOfPoints):
    point = list(map(int, input().split()));
    points.append(point);

def sortX(point):
    return point[0];

def sortY(point):
    return point[1];

points.sort(key = sortX);

def minDistanceInStrip(initialSetPoints, d):
    filteredPoints = [point for point in initialSetPoints if point[0] < d];
    minimumDistance = d;
    numberOfFilteredPoints = len(filteredPoints);
    for i in range(len(filteredPoints)):
        for j in range(i+1, len(filteredPoints)):
            dist = distance(filteredPoints[i][0], filteredPoints[i][1], filteredPoints[j][0], filteredPoints[j][1]);
            if dist < minimumDistance:
                minimumDistance = dist
    return minimumDistance;

def minDistNaive(pointsList):
    minimumDistance = 99999999999;
    for i in range(len(pointsList)):
        for j in range(i+1, len(pointsList)):
            dist = distance(pointsList[i][0], pointsList[i][1], pointsList[j][0], pointsList[j][1]);
            if dist < minimumDistance:
                minimumDistance = dist;
    return minimumDistance;

def minDistance(pointsList):
    middlePointIndex = int(len(pointsList) / 2);
    set1 = pointsList[0: middlePointIndex];
    set2 = pointsList[middlePointIndex:];
    if(len(set1) <= 2 or len(set2) <= 2):
        return minDistanceInStrip(pointsList, minDistNaive(pointsList));
    d1 = minDistance(set1);
    d2 = minDistance(set2);
    return minDistanceInStrip(pointsList, min(d1, d2));

print(minDistance(points));
