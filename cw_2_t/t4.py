import threading


def fact(start, end, q):
    f = 1
    for n in range(start, end+1):
        f *= n

    q.append(f)

def main():
    q = []
    ts = []
    c_t = int(input("Введите количество потоков: "))
    n = int(input("Введите число, факториал которого хотите получить: "))
    step = c_t if c_t < n else n
    
    for i in range(1, (n+1), n//step):
        l_start = i
        l_end = i+n//step if i+n//step < n+1 else n+1
        
        ts.append(threading.Thread(target=fact, args=(l_start, l_end-1, q, )))

    for t in ts:
        t.start()
        t.join()

    result = 1
    for n in q:
        result *= n

    print(result)




if __name__ == '__main__':

    main()