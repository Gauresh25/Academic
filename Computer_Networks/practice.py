data = "1010101".strip()
recd=[int(bit) for bit in data]

# for i in recd:
#     print(type(i))

def calc_par(received,pos,size):

    parity=0
    for i in range(1,size+1):
        if i & pos  :#here we filter out the redundant bits
            if received[size-i]==1:
                parity +=1

    return parity%2


def check_hamm(received):
    size = len(received)
    err_pos =0

    for i in range(size):
        if 2**i < size:
            par = calc_par(received,2**i,size)

            if par!=0:
                err_pos+=2**i

    return err_pos

print(check_hamm(recd))