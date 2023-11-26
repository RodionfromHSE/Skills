# dataclass
from dataclasses import dataclass, field
from collections import deque, defaultdict
# logger
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class MinHeap:
    def __init__(self) -> None:
        self.data = [None]
        self.size = 0

    def __len__(self):
        return self.size
    
    def _sift_up(self, index):
        while (parent := index // 2) > 0 and self.data[parent] > self.data[index]:
            self.data[index], self.data[parent] = self.data[parent], self.data[index]
            index = parent

    def _sift_down(self, index):
        son = index * 2
        if son > self.size:
            return
        if son + 1 <= self.size and self.data[son + 1] < self.data[son]:
            son += 1

        if self.data[index] > self.data[son]:
            self.data[index], self.data[son] = self.data[son], self.data[index]
            self._sift_down(son)

    def insert(self, value):
        self.data.append(value)
        self.size += 1
        self._sift_up(self.size)

    def extract(self):
        self.data[1], self.data[self.size] = self.data[self.size], self.data[1]
        self.size -= 1
        self._sift_down(1)
        return self.data.pop()

def main():
    queries = [
        "add 3",
        "add 2",
        "add 1",
        "add 1",
        "add 1",
        "extract",
        "extract",
        "extract",
        "add 0",
        "add 5",
        "extract"
    ]

    heap = MinHeap()
    for q in queries:
        print(q)
        if q == "extract":
            print(heap.extract())
        else:
            heap.insert(int(q.split()[1]))
        print(heap.data)
        
            

    


if __name__ == '__main__':
    main()