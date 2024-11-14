import threading


def sort_arr(arr, q):
    
    arr.sort() # не важно, как сортируются подмассивы

    q.append(arr)

def main():
    q = []
    ts = []
    
    array = [949, 748, 115, 675, 801, 979, 311, 651, 287, 388, 154, 225, 909, 969, 267, 893, 863, 148, 887, 342,
180, 109, 263, 486, 216, 198, 256, 642, 993, 173, 59, 311, 163, 490, 917, 74, 485, 790, 371, 758,
471, 985, 470, 59, 581, 76, 844, 84, 645, 97, 234, 602, 551, 810, 303, 439, 825, 971, 264, 415,
581, 379, 854, 768, 0, 2, 248, 364, 195, 863, 89, 688, 42, 705, 747, 38, 662, 755, 440, 945, 548,
205, 225, 194, 833, 318, 119, 412, 762, 440, 470, 963, 508, 554, 932, 270, 312, 228, 442, 691]

    n = len(array)

    for i in range(0, n, n//10):
        l_start = i
        l_end = i+n//10 if i+n//10 < n+1 else n+1
        
        ts.append(threading.Thread(target=sort_arr, args=(array[l_start: l_end], q, )))

    for t in ts:
        t.start()
        t.join()

    result = []

    while q:
        el = min(q, key=lambda x: x[0])
        if el:
            result.append(el.pop(0))
            if not el: q.remove(el)
    

    print(result)

        




if __name__ == '__main__':

    main()