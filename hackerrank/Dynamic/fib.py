__author__ = 'chamathsilva'

def fib(num):
    if num<2:
        return num
    else:
        return fib(num-1)+fib(num-2)

#print(fib(40))

def fib1(num):
    lst=[1,1,1]
    for i in range(3,num+1):
        lst.append(lst[-1]+lst[-2])
    print(lst[-1])

fib1(500)