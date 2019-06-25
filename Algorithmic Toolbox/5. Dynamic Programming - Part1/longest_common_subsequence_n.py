# Source code in python3
from itertools import product
import numpy as np

def neighbors(index):
    N = len(index)
    for relative_index in product((0, -1), repeat=N):
        if not all(i == 0 for i in relative_index):
            yield tuple(i + i_rel for i, i_rel in zip(index, relative_index))

def longestCommonSubSequenceOfN(sqs):
    numberOfSequences = len(sqs);
    lengths = np.array([len(sequence) for sequence in sqs]);
    incrLengths = lengths + 1;
    lengths = tuple(lengths);
    inverseDistances = np.zeros(incrLengths);
    ranges = [tuple(range(1, length+1)) for length in lengths[::-1]];
    for tupleIndex in product(*ranges):
        tupleIndex = tupleIndex[::-1];
        neighborIndexes = list(neighbors(tupleIndex));
        operationsWithMisMatch = np.array([]);
        for neighborIndex in neighborIndexes:
            operationsWithMisMatch = np.append(operationsWithMisMatch, inverseDistances[neighborIndex]);
        operationsWithMatch = np.copy(operationsWithMisMatch);
        operationsWithMatch[-1] = operationsWithMatch[-1] + 1;
        chars = [sqs[i][neighborIndexes[-1][i]] for i in range(numberOfSequences)];
        if(all(elem == chars[0] for elem in chars)):
            inverseDistances[tupleIndex] = max(operationsWithMatch);
        else:
            inverseDistances[tupleIndex] = max(operationsWithMisMatch);
        # pdb.set_trace();

    subString = "";
    mainTupleIndex = lengths;
    while(all(ind > 0 for ind in mainTupleIndex)):
        neighborsIndexes = list(neighbors(mainTupleIndex));
        anyOperation = False;
        for tupleIndex in neighborsIndexes:
            current = inverseDistances[mainTupleIndex];
            if(current == inverseDistances[tupleIndex]):
                mainTupleIndex = tupleIndex;
                anyOperation = True;
                break;
        if(not anyOperation):
            subString += str(sqs[0][mainTupleIndex[0] - 1]);
            mainTupleIndex = neighborsIndexes[-1];
    return subString[::-1];

numberOfSequences = int(input("Enter the number of sequences: "));
sequences = [input("Enter sequence {} : ".format(i)) for i in range(1, numberOfSequences + 1)];
print(longestCommonSubSequenceOfN(sequences));