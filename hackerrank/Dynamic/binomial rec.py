
__author__ = 'chamathsilva'


def binomial_coefficient(n, r):
    if (r == 0) or (n == r):
        return 1
    else:
        return binomial_coefficient(n-1, r-1) + binomial_coefficient(n-1, r)





if __name__ == '__main__':
    #print(binomial_coefficient(5,2))
    print(binomial_coefficient(34,23))








