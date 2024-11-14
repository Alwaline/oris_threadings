import threading

def work():
    pass

def main():
    threadings = []
    for _ in range(10):
        threadings.append(threading.Thread(target=work))

    for thread in threadings:
        print(thread.getName)


if __name__ == '__main__':
    main()