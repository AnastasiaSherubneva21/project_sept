import os
import time
import threading
from multiprocessing import Process


class Dinamic_Graph:

    def __init__(self, filename):
        self.filename = filename

    def calculate_and_output(self):
        with open(self.filename) as fn:
            strings = fn.readlines()
        for i in strings:
            lst = i.split()
            date = lst[2][6:] + '.' + lst[2][4:6] + '.' + lst[2][0:4]
            val_2 = float(lst[4])
            if strings.index(i) == 0:
                val_1 = val_2
                delta = 0
            else:
                val_0 = val_1
                val_1 = val_2
                delta = val_2 - val_0
            points = int(delta*10)
            if abs(points) > 50:
                points = 50
            if points < 0:
                print('pr=' + str(os.getpid()) + ' ' + 'th=' + str(threading.current_thread().ident) + ' |   ' + date + ' '*3 + '<--' + ' '*(51+points) + '.'*(-points) + '|')
            else:
                print('pr=' + str(os.getpid()) + ' ' + 'th=' + str(threading.current_thread().ident) + ' |   ' + date + ' '*3 + '-->' + ' '*51 + '|' + '.'*points)

    def processing(self):
        p = Process(target=self.calculate_and_output, args=())
        p.start()
        p.join()


def main(classname):
    time_1 = time.time()
    dg = classname('USD_CB.txt')
    dg.processing()
    time_2 = time.time()
    print(' \n \n \n', ' ' * 60, 'Время работы программы: ', time_2 - time_1)


if __name__ == '__main__':
    main(Dinamic_Graph)
