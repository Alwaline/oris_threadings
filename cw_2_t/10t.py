import threading

class Parking:
    def __init__(self, spaces=3):
        self.sem = threading.Semaphore(spaces)
        self.cars = {}

    def add_car(self, car, time):
        print(f"Машина {car} хочет занять парковочное место")
        self.sem.acquire()
        print(f"Машина {car} заняла парковочное место на {time} минут")
        self.cars[car] = threading.Timer(time, self.del_car, args=(car,))
        self.cars[car].start()

    
    def del_car(self, car):
        print(f"Машина {car} освободила парковочное место")
        self.sem.release()
            
    


def main():
    p = Parking()

    p.add_car('car1', 8)
    p.add_car('car2', 10)
    p.add_car('car3', 10)
    p.add_car('car4', 4)
    p.add_car('car5', 30)
    p.add_car('car6', 1)
    


if __name__ == '__main__':
    main()