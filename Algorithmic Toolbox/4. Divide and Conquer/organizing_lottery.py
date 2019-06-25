# Source code in python3
numberOfSegments, numberOfPoints = map(int, input().split());
segmentsRange = [];
points = [];

for i in range(numberOfSegments):
    segmentsRange.append(list(map(int, input().split())));
points = list(map(int, input().split()));
combinedElements = [];

for segment in segmentsRange:
    combinedElements.append([segment[0], 1]);
    combinedElements.append([segment[1], 3]);

for point in points:
    combinedElements.append([point, 2]);

combinedElements = sorted(combinedElements, key = lambda x: (x[0], x[1]));
finalCounts = dict();
countSegments = 0;

for point in points:
    finalCounts[point] = 0;

for combinedElement in combinedElements:
    if(combinedElement[1] == 1):
        countSegments += 1;
    elif(combinedElement[1] == 3):
        countSegments -= 1;
    else:
        finalCounts[combinedElement[0]] = countSegments;

sequenceCounts = [finalCounts[point] for point in points];
print(*sequenceCounts);