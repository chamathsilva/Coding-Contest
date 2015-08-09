__author__ = 'chamathsilva'

for _ in range(int(input())):
    String = input()
    index = 0
    deletion = 0
    length = len(String)
    while index < length:
        if String[index] == 'A':
            next_index = String.find('B', index+1)
        else:
            next_index = String.find('A', index+1)

        if next_index == -1:
            deletion += (length - index)-1
            break
        else:
            deletion += (next_index - index)-1
            index = next_index

    print(deletion)