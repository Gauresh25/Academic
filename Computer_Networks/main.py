no_bits=int(input("Enter number of bits in sequence number"))
seq_len = pow(2,no_bits)

no_frames = int(input("Enter number of frames to send"))

li=[]
for i in range(0,no_frames):
    li.append(i%seq_len)

print(li)

s_win = pow(2,no_bits)-1

err_fr=int(input("Enter position of error bit"))

for 