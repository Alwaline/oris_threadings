import threading
import time

balance = 0
lock = threading.Lock()

def change_balance(s):
    global balance

    while s < 0 and balance + s < 0:
        continue
    else:
        with lock:
            print(f"Сейчас на балансе {balance} деняг")

            m = "Прибавляю" if s > 0 else "Трачу"

            balance += s

            print(f"{m} {s} деняг")


            print(f"Теперь на балансе {balance} деняг")

            time.sleep(1)
            

def main():
    threadings = []
    
    threadings.append(threading.Thread(target=change_balance, args=(1000, )))
    threadings.append(threading.Thread(target=change_balance, args=(-500, )))
    threadings.append(threading.Thread(target=change_balance, args=(-200, )))
    threadings.append(threading.Thread(target=change_balance, args=(-400, )))
    threadings.append(threading.Thread(target=change_balance, args=(1000, )))
    threadings.append(threading.Thread(target=change_balance, args=(1000, )))
    threadings.append(threading.Thread(target=change_balance, args=(-2900, )))
    threadings.append(threading.Thread(target=change_balance, args=(1000, )))
    
    for t in threadings:
        t.start()

    

if __name__ == '__main__':
    main()