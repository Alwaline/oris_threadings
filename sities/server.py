import socket
import threading
import time

# Константы
HOST = '127.0.0.1'  # Адрес сервера
PORT = 10001        # Порт сервера


clients = []

# создаем сокет
# подключемся к серверному сокету

def notify(data, conn, name):
    for client in clients:
        if client[1] != conn:
            client[1].send(f"{name}: {data.decode()}".encode())


def check_data(data, conn, name):
    if data.decode() == 'yaproigral':
        message = f'Соперник {name} долго думал и проиграл. Вы победили!'.encode()
        notify(message, conn, name)
        return True
    return False

def handle_client(name, conn, addr, sem):
    with sem:
        print(f'Подключен {addr}')

        while len(clients) < 2:
            time.sleep(5)
        else:
            conn.send('Соперник подключился\n'.encode())
            clients[0][1].send('Вы печатаете первый\n'.encode())

        while True:
            data = conn.recv(1024)
            if not data or check_data(data, conn, name): break
            notify(data, conn, name)
            

        conn.close()
        clients.remove((name, conn, addr))
        print(f"Закрыто соединение с {addr}")

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen(2)
        print(f'Сервер запущен и ждёт соединений на {HOST}:{PORT}')
        sem = threading.Semaphore(2)
        while True:
            conn, addr = server_socket.accept()
            name = conn.recv(1024).decode()

            if len(clients) < 2:
                clients.append((name, conn, addr))
                thread = threading.Thread(target=handle_client, args=(name, conn, addr, sem))
                thread.start()
            else:
                conn.close()




if __name__ == '__main__':
    start_server()