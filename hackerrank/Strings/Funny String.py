__author__ = 'chamathsilva'
for _ in range(int(input())):
    string = input()

    i = 1
    N = len(string)
    while i < N:
        if abs(ord(string[i])-ord(string[i-1])) == abs(ord(string[-(i+1)])-ord(string[-(i+1)+1])):
            i += 1
        else:
            break

    print(["Not Funny","Funny"][i == N])

