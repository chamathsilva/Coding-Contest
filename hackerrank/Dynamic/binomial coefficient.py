__author__ = 'chamathsilva'


def binomial_coefficient(n, r):
    T = [[0 for j in range(r+1)] for i in range(n+1)]

    for i in range(0,n-r+1):
        T[i][0] = 1
    for i in range (1,r+1):
        T[i][i] = 1
    for j in range (1,r+1):
        for i in range(j+1,n-r+j+1):
            T[i][j] = T[i-1][j-1] + T[i-1][j]

    print(T[n][r])
    print_matrix(T)


def print_matrix(matrix):
    for i in matrix:
        for j in i:
            print("%3d"%j, end=" ")
        print("")



binomial_coefficient(34,23)

