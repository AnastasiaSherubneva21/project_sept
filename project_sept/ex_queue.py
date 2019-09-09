from ex_process import Dinamic_Graph, main
from concurrent.futures import ThreadPoolExecutor


class Dinamic_Graph_2(Dinamic_Graph):

    def processing(self):
        with ThreadPoolExecutor(max_workers=5) as tpe:
            tpe.submit(self.calculate_and_output)


if __name__ == '__main__':
    main(Dinamic_Graph_2)
