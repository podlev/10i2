def to_10(n,o1):
    power = len(n) - 1 
    s = 0
    for digit in n:
        if '0' <= digit <= '9':
            s += int(digit) * (o1 ** power)
        else:
            s += (ord(digit)-ord('A')+10) * (o1 ** power) 
        power -= 1
    return s

def to_o2(n,o2):
    s = ''
    while(n != 0):
        digit = n % o2
        #print(digit)
        if 0 <= digit <= 9:
            s += str(digit)
        else:
            s += chr(digit+ord('A')-10)
        n //= o2
    return s[::-1]
        


n = input()
o1, o2 = map(int,input().split())

n_10 = int(to_10(n,o1))
#print(n_10)
print(to_o2(n_10,o2))
