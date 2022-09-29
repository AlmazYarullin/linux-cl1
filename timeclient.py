import socket


PORT = 1303


def main():
    host = input('Enter server ip: ')

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, PORT))
        data = s.recv(1024)
        print('Received from server:', data.decode('utf-8'))


if __name__ == '__main__':
    main()
