import socket

def main():
    c = socket.socket()
    c.connect(('localhost', 9999))

    num1 = int(input('Enter number 1: '))
    num2 = int(input('Enter number 2: '))

    c.send(str(num1).encode())
    c.send(str(num2).encode())

    result = c.recv(1024).decode()
    print(f'Result from server: {result}')

    c.close()

if __name__ == '__main__':
    main()