import re,string
regex = re.compile('[%s]' % re.escape(string.punctuation))


for _ in range(int(input())):
    if "31415926535897932384626433833".startswith(''.join(map(lambda x:str(len(x)), regex.sub('',input()).split()))):
        print("It's a pi song.")
    else:
        print("It's not a pi song.")

