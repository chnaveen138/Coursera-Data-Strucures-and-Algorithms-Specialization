# Source code in python3
def longestCommonSubSequenceOfTwo(n, seq1, m, seq2):
    inverseDistances=[[0 for j in range(m+1)] for i in range(n+1)]
    for j in range(1, m+1):
        for i in range(1, n+1):
            insertion = inverseDistances[i-1][j];
            deletion = inverseDistances[i][j-1];
            mismatch = inverseDistances[i-1][j-1];
            match = inverseDistances[i-1][j-1] + 1;
            if(seq1[i-1] == seq2[j-1]):
                inverseDistances[i][j] = max(insertion, deletion, match);
            else:
                inverseDistances[i][j] = max(insertion,deletion, mismatch);
    return inverseDistances[n][m];
n = int(input());
seq1 = list(map(int, input().split()));
m = int(input());
seq2 = list(map(int, input().split()));
print(longestCommonSubSequenceOfTwo(n, seq1, m, seq2));