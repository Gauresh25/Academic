exp =  "a=r+t*s*q*s"

lhs,rhs = exp.split("=")
add_parts = rhs.split("+")
print(add_parts)

tc = 1
for i in range(len(add_parts)):
    mult_par = add_parts[i].split("*")
    print(mult_par)
    while len(mult_par)>1:
        tempc = 't'+str(tc)
        print(f"{tempc} = {mult_par[0]} * {mult_par[1]}")
        mult_par[0]=tempc
        mult_par.pop(1)
        tc = tc+1
        add_parts[i]=tempc

while len(add_parts)>1:
    tempc = 't' + str(tc)
    print(f"{tempc} = {add_parts[0]} + {add_parts[1]}")
    add_parts[0] = tempc
    add_parts.pop(1)
    tc = tc + 1

print(add_parts)