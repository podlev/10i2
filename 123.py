def to_o2(n,o2):
    s = ''
    while(n != 0):
        digit = n % o2
        #print(digit)
        if 0 <= digit <= 9:
            s += str(digit)
        else:
            #доделать
            pass
        n //= o2
    return s[::-1]
        
n = input()
o2 = int(input())

for i in range(0,len(n)**o2):
    ss=''
    k = to_o2(i,o2)
    for j in k:
        ss += (n[int(j)])
    print(ss)
