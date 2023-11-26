# dataclass
from dataclasses import dataclass, field
from collections import deque, defaultdict
# logger
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

@dataclass
class Client:
    arrival_t: int
    item: int = field(compare=False)

    

def main():
    n = int(input())
    queue = deque()
    items = defaultdict(int)
    def clean_queue(t):
        nonlocal queue, items
        while queue:
            first = queue[0]
            if items[first.item] > 0:
                wait_t = t - first.arrival_t
                items[first.item] -= 1
                print(wait_t)
                queue.popleft()
            else:
                break

    for _ in range(n):
        type, t, item = map(int, input().split())
        if type == 1:  # good arrival
            items[item] += 1
        else:
            queue.append(Client(t, item))
        clean_queue(t)

    left_clients = len(queue)
    for _ in range(left_clients):
        print(-1)


if __name__ == '__main__':
    main()