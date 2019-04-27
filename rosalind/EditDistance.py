def edit_distance(firstWord, secondWord):
    M = [[0 for j in xrange(len(secondWord) + 1)] for i in xrange(len(firstWord) + 1)]
    for i in range(1, len(firstWord)+1):
        M[i][0] = i
    for j in range(1, len(secondWord)+1):
        M[0][j] = j

    for i in xrange(1, len(firstWord)+1):
        for j in xrange(1, len(secondWord)+1):
            if firstWord[i-1] == secondWord[j-1]:
                M[i][j] = M[i-1][j-1]
            else:
                M[i][j] = min(M[i-1][j]+1, M[i][j-1]+1, M[i-1][j-1]+1)

    return M[len(firstWord)][len(secondWord)]