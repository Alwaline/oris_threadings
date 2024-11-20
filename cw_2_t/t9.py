import threading
import math

def calculate_factorial(n, results, key):
    try:
        if n < 0:
            raise ValueError("Факториал определен только для неотрицательных чисел.")
        results[key] = math.factorial(n)
    except Exception as e:
        results[key] = f"Ошибка: {e}"


def calculate_power(base, exponent, results, key):
    try:
        results[key] = math.pow(base, exponent)
    except Exception as e:
        results[key] = f"Ошибка: {e}"


class Calulator:
    def __init__(self):
        self.results = {}
        self.threads = []

    def add_task(self, func, *args):
        key = f"Task-{len(self.threads)+1}"
        t = threading.Thread(target=func, args=(*args, self.results, key))
        self.threads.append(t)

    def execute(self):
        for t in self.threads:
            t.start()
            t.join()
        
    def get_results(self):
        return self.results
    

def main():
    calc = Calulator()
    
    calc.add_task(calculate_factorial, 7)
    calc.add_task(calculate_power, 3, 5)

    calc.execute()

    for task, res in calc.get_results().items():
        print(task, res)


if __name__ == '__main__':
    main()