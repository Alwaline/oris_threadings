import socket
import threading

# создаем сокет
# подключемся к серверному сокету

# Константы
HOST = '127.0.0.1'  # Адрес сервера
PORT = 10001        # Порт сервера


use_sities = []
is_lose = False

def lose(sock):
    print('Вы долго думали и проиграли...')
    sock.send('yaproigral'.encode())
    exit()


def check_sity(sity):
    if sity in use_sities:
        print(f"Город {sity} уже называли")
        return False
    elif use_sities and sity[0] != use_sities[-1][-1]:
        print(f'Город должен начинаться на "{use_sities[-1][-1]}"')
        return False
    use_sities.append(sity)
    return True

def add_city(data: str):
    if data.find(':') >= 0:
        use_sities.append(data[data.find(':')+1:])

def one_round(sock):
    message = "Введите сообщение (или 'exit' для выхода):"
    while message != 'exit':

        data = sock.recv(1024)
        if data:
            print("\n", data.decode(), "\n")
            add_city(data.decode())

        timeout = threading.Timer(60.0, lose, (sock,))
        timeout.start()
        
        try:
            message = input().lower().strip()
            if timeout.is_alive():
                if message.lower() == 'exit':
                    break
                while not check_sity(message):
                    message = input().lower().strip()
                sock.send(message.encode())
                timeout.cancel()
            else:
                break
        except:
            pass


    sock.close()

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))

    print("Добро пожаловать в игру \"Города\"")

    name = input("Введите ваше имя: ")
    sock.send(name.encode("utf-8"))

    data = sock.recv(1024).decode()
    if data:
        print("Подключено к серверу.")
        print("Игра началась")


        # Запускаем потоки для отправки и получения сообщений
        thread_game = threading.Thread(target=one_round, args=(sock,), daemon=True)
        thread_game.start()
        thread_game.join()



if __name__ == "__main__":
    main()