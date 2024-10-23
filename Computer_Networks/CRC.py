def xor(a, b):
    result = ""
    for i in range(len(b)):
        if a[i] == b[i]:
            result += "0"
        else:
            result += "1"
    return result


def mod2div(dividend, divisor):
    pick = len(divisor)
    tmp = dividend[0: pick]

    while pick < len(dividend):
        if tmp[0] == '1':
            tmp = xor(divisor, tmp) + dividend[pick]
        else:
            tmp = xor('0' * pick, tmp) + dividend[pick]
        tmp = tmp[1:]  # Remove the first bit after each step
        pick += 1

    if tmp[0] == '1':
        tmp = xor(divisor, tmp)
    else:
        tmp = xor('0' * pick, tmp)

    print("remanider:")
    print(tmp)

    return tmp[-(len(divisor)-1):]  # Remove leading zeros


def encode_data(data, key):
    appended_data = data + '0' * (len(key) - 1)
    remainder = mod2div(appended_data, key)
    return data + remainder  # Ensure remainder is correct length


def check_data(encoded_data, key):
    remainder = mod2div(encoded_data, key)
    return remainder == '0' * (len(key) - 1)


# Main program
data = input("Enter data (message): ")
key = input("Enter key (divisor): ")

print("Sender side...")
appended_data = data + '0' * (len(key) - 1)
print(f"Appended Data: {appended_data}")

remainder = mod2div(appended_data, key)
print(f"Remainder: {remainder}")

encoded_data = encode_data(data, key)
print(f"Encoded Data (Data + Remainder): {encoded_data}")

print("Receiver side...")
if check_data(encoded_data, key):
    print("Correct message received")
else:
    print("Error in transmission")