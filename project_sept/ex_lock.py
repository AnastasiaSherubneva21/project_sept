from threading import Lock, current_thread
from ex_queue import Dinamic_Graph_2, main

lock = Lock()


class Dinamic_Graph_3(Dinamic_Graph_2):

    def __init__(self, filename):
        lock.acquire()
        with open(filename) as fn:
            strings = fn.readlines()
        self.strings = strings
        lock.release()


if __name__ == '__main__':
    main(Dinamic_Graph_3)
