__author__ = 'chamathsilva'

print(["not pangram","pangram"][len(set(list(input().replace(" ","").lower())))==26])