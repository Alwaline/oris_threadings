import threading
import os

class FileSearcher(threading.Thread):

    def __init__(self, dir, pattern, sem, results):
        super().__init__()
        self.dir = dir
        self.pattern = pattern
        self.sem = sem
        self.results = results


    def run(self):
        with self.sem:
            found_files = []
            for root, _, files in os.walk(self.dir):
                for file in files:
                    if file.endswith(self.pattern):
                        found_files.append(os.path.join(root, file))
            
            self.results.extend(found_files)



def find_file_by_ext(dirs, pattern, max_threads=4):
    sem = threading.Semaphore(max_threads)
    results = []
    ts = []
    
    for dir in dirs:
        t = FileSearcher(dir, pattern, sem, results)
        ts.append(t)
        t.start()

    for t in ts:
        t.join()

    return results


def main():
    dirs = ['/home/alwalone/Загрузки']
    pattern = '.txt'

    max_threads = 4

    found_files = find_file_by_ext(dirs, pattern, max_threads)
    
    for file in found_files:
        print(file)

if __name__ == '__main__':
    main()