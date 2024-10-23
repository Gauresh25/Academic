def PosCalc(a, b ,c):
    s1 = str(a)
    s2 = str(b)
    s3 = str(c)
    s = s1 + s2 +s3
    c = int(s,2)
    return c

d7,d6,d5,p4,d3,p2,p1 = map(int, input("Enter 7 bit code values: ").split())
#print(type(d7))
# 1 0 0 0 1 1 0
#1 1 0 0 1 1 0
flag =0
if(p1 != d3^d5^d7):
    p1 = 1
    flag = 1
if (p2 != d3 ^ d6 ^ d7):
    p2 = 1
    flag = 1
if(p4 != d5^d6^d7):
    p4 = 1
    flag = 1

if(flag == 1):
    print("Error detected at position:")
    p = PosCalc(p4,p2,p1)
    print(p4, p2, p1)
    print(p)
else:
    print("No Error")