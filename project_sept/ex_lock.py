import os
from threading import Lock, current_thread
from ex_queue import Dinamic_Graph_2, main

lock = Lock()


class Dinamic_Graph_3(Dinamic_Graph_2):

    def calculate_and_output(self):
        lock.acquire()
        with open(self.filename) as fn:
            strings = fn.readlines()
        lock.release()
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
                print('pr=' + str(os.getpid()) + ' ' + 'th=' + str(current_thread().ident) + ' |   ' + date + ' '*3 + '<--' + ' '*(51+points) + '.'*(-points) + '|')
            else:
                print('pr=' + str(os.getpid()) + ' ' + 'th=' + str(current_thread().ident) + ' |   ' + date + ' '*3 + '-->' + ' '*51 + '|' + '.'*points)


if __name__ == '__main__':
    main(Dinamic_Graph_3)
