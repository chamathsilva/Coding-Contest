__author__ = 'chamathsilva'

for _ in range(int(input())):
    N = int(input())
    num_array = list(map(int, input().split()))

    index = 0
    out = False
    left_sum = sum(num_array[:index])
    right_sum = sum(num_array[index+1:])
    if left_sum == right_sum:
        out = True
    while index < N-1:
        if left_sum == right_sum:
            out = True
            break
        elif left_sum > right_sum:
            out = False
            break

        left_sum += num_array[index]
        right_sum -= num_array[index+1]
        index += 1

    print(["NO", "YES"][out])
