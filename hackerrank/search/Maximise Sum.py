__author__ = 'chamathsilva'



#not done

def max_subarray(A,K):
    max_ending_here = max_so_far = 0
    for x in A:
        max_ending_here = max(0, (max_ending_here + x) % K)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far


for _ in range(int(input())):
    N, M = map(int, input().split())
    array = list(map(int,input().split()))
    print(max_subarray(array,M))