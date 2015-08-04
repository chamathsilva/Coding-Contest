__author__ = 'chamathsilva'


for i in range(int(input())):
    n, k = map(int, input().split())
    present_count = filter(lambda x:x <= 0 , map(int,input().split()))
    print(["YES","NO"][len(list(present_count)) >= k])