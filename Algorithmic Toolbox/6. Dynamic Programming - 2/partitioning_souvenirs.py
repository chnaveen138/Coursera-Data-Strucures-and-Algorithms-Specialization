# Source code in python3
import itertools

def partitions(souvenirs):
    for partition in itertools.product(range(3), repeat=len(souvenirs)):
        producedSums = [None] * 3
        for i in range(3):
            producedSums[i] = sum(souvenirs[j] for j in range(len(souvenirs)) if partition[j] == i)
        if producedSums[0] == producedSums[1] and producedSums[1] == producedSums[2]:
            return 1
    return 0

numberOfWeights = int(input());
souvenirs = list(map(int, input().split()))
print(partitions(souvenirs))