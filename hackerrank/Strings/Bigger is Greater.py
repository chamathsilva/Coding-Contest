__author__ = 'chamathsilva'

string1 = "hefg"
temp = sorted(set(string1))

if len(temp) == 1:
    print("no answer")
else:
    index = len(string1)-1
    while index >= 0:
        for i in temp:
            if i > string1[index]:
                index2 = string1.find(i)
                temp = list(string1)
                (temp[index], temp[index2]) = (temp[index2], temp[index])
                print(''.join(temp))
                break
        index -= 1
    print("no answer")





