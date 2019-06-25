# Source code in python3
def longestCommonSubSequenceOfThree(n, seq1, m, seq2, l, seq3):
    inverseDistances=[[[0 for k in range(l+1)] for j in range(m+1)] for i in range(n+1)]
    for k in range(1, l+1):
        for j in range(1, m+1):
            for i in range(1, n+1):
                insertion1 = inverseDistances[i-1][j][k];
                insertion2 = inverseDistances[i][j-1][k];
                insertion3 = inverseDistances[i][j][k-1];
                deletion1 = inverseDistances[i-1][j-1][k];
                deletion2 = inverseDistances[i-1][j][k-1];
                deletion3 = inverseDistances[i][j-1][k-1];
                mismatch = inverseDistances[i-1][j-1][k-1];
                match = inverseDistances[i-1][j-1][k-1] + 1;
                if(seq1[i-1] == seq2[j-1] == seq3[k-1]):
                    inverseDistances[i][j][k] = max(insertion1, insertion2, insertion3, deletion1, deletion2, deletion3, match);
                else:
                    inverseDistances[i][j][k] = max(insertion1, insertion2, insertion3, deletion1, deletion2, deletion3, mismatch);
    return inverseDistances[n][m][l];
n = int(input());
seq1 = list(map(int, input().split()));
m = int(input());
seq2 = list(map(int, input().split()));
l = int(input());
seq3 = list(map(int, input().split()));
print(longestCommonSubSequenceOfThree(n, seq1, m, seq2, l, seq3));