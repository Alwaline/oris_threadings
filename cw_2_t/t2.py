import threading

def primary(start, end):

    for n in range(start, end+1):
        for i in range(2, round(n**0.5)+1):
            if n % i == 0:
                break
        else:
            print(n)
        


        


def main():
    threadings = []
    start = 1
    end = 10
    n = end - start
    for i in range(start, end, (end-start)//10+1):
        l_start = i
        l_end = i+(end-start)//10 if i+(end-start)//10 < n else end
        threadings.append(threading.Thread(target=primary, args=(l_start, l_end ,)))

    for t in threadings:
        t.start()
        t.join()



if __name__ == '__main__':
    main()