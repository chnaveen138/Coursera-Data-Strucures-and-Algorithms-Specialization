# Source code in python3
def editDistance(str1, str2):
    n = len(str1);
    m = len(str2);
    distances=[[0 for j in range(m+1)] for i in range(n+1)]
    for i in range(n+1):
        distances[i][0] = i;
    for j in range(m+1):
        distances[0][j] = j;
    for j in range(1, m+1):
        for i in range(1, n+1):
            insertion = distances[i-1][j] + 1;
            deletion = distances[i][j-1] + 1;
            mismatch = distances[i-1][j-1] +1;
            match = distances[i-1][j-1];
            if(str1[i-1] == str2[j-1]):
                distances[i][j] = min(insertion, deletion, match);
            else:
                distances[i][j] = min(insertion,deletion, mismatch);
    return distances[n][m];
str1 = input();
str2 = input();
print(editDistance(str1, str2));