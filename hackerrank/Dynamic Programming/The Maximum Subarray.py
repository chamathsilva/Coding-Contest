__author__ = 'chamathsilva'


#Kadane algorithm
def max_subarray(A):
    max_ending_here = max_so_far = A[0]
    for x in A[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far


def max_non_contiguous(A):
    min_min_so_far = - float("inf")
    max_so_far = 0
    state = False
    for i in A:
        if i > 0:
            state = True
            max_so_far += i
        else:
            if i > min_min_so_far:
                min_min_so_far = i

    if state:
        return max_so_far
    else:
        return min_min_so_far

for _ in range(int(input())):
    N = input()
    Array = list(map(int,input().split()))
    print(max_subarray(Array),max_non_contiguous(Array))