import threading
import re
from collections import Counter

def count_words(text):
    data = re.findall(r'\w+', text.lower())
    return Counter(data)


def read_chunk(filename, start, chunk, res, i):
    with open(filename) as file:
        pos = file.seek(start)

        if start > 0:
            file.seek(file.tell()-1)
            char = file.read(1)
            while char.isalpha():
                char = file.read(1)
                chunk -= 1
   
        data = file.read(chunk)

        if data[-1].isalpha():
            char = file.read(1)
            while char.isalpha():
                data += char
                char = file.read(1)

    res[i] = count_words(data)


def main():
    c_t = 10

    filename = input('Введите название файла: ')
    
    with open(filename) as file:
        size = file.seek(0, 2)
        chunk = size // c_t

    res = [None] * c_t

    ts = []
    for i in range(c_t):
        start = i * chunk
        ts.append(threading.Thread(target=read_chunk, args=(filename, start, chunk, res, i,)))

    for t in ts:
        t.start()
        t.join()

    ans = Counter()
    for c in res:
        ans.update(c)

    for word, count in ans.most_common():
        print(f'{word} : {count}')

if __name__ == '__main__':
    main()