# Heap code


class BinHeap:
    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0

    def perc_up(self, i):
        while i // 2 > 0:
            if self.heap_list[i] < self.heap_list[i // 2]:
                tmp = self.heap_list[i // 2]
                self.heap_list[i // 2] = self.heap_list[i]
                self.heap_list[i] = tmp
            i = i // 2


    def insert(self, k):
        for item in k:
            self.heap_list.append(item)
            self.current_size = self.current_size + 1
            self.perc_up(self.current_size)

    def __str__(self):
        return str(self.heap_list)
