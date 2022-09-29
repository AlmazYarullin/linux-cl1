import socket
import datetime

HOST = '0.0.0.0'
PORT = 1303


def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(1)
        while True:
            try:
                conn, addr = s.accept()
            except KeyboardInterrupt:
                break
            with conn:
                current_date = datetime.datetime.now().strftime("%d.%m.%Y %H:%M")
                conn.sendall(current_date.encode('utf-8'))


if __name__ == '__main__':
    start_server()
