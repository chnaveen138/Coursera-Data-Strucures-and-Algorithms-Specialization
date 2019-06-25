# Source code in python3
def KnapsackWithoutRepetitions(weightCapacity, weights, values):
    numberOfWeights = len(weights);
    maxValues = [[0 for i in range(0, numberOfWeights + 1)] for j in range(0, weightCapacity + 1)]
    for i in range(1, numberOfWeights + 1):
        for w in range(1, weightCapacity + 1):
            maxValues[w][i] = maxValues[w][i-1];
            if(weights[i-1] <= w):
                value = maxValues[w - weights[i-1]][i-1] + values[i-1];
                if(maxValues[w][i] < value):
                    maxValues[w][i] = value;
    return maxValues[weightCapacity][numberOfWeights];
weightCapacity, numberOfWeightBars = map(int, input().split());
weights = list(map(int, input().split()));
values = weights.copy();
maxValuePossible = KnapsackWithoutRepetitions(weightCapacity, weights, values);
print(maxValuePossible);