import threading


def fact(start, end, q):
    f = 1
    for n in range(start, end+1):
        f *= n

    q.append(f)

def main():
    q = []
    ts = []
    n = 10
    for i in range(1, (n+1), n//10):
        l_start = i
        l_end = i+n//10 if i+n//10 < n+1 else n+1
        
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