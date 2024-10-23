import socket

def main():
    s = socket.socket()
    s.bind(('localhost', 9999))
    s.listen(2)
    print('Server is running')

    while True:
        c, address = s.accept()
        print(f'Client {address} connected')

        num1 = int(c.recv(1024).decode())
        num2 = int(c.recv(1024).decode())
        result = num1 + num2

        c.send(str(result).encode())
        c.close()
        print('Client disconnected')

if __name__ == '__main__':
    main()