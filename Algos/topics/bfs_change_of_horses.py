from dataclasses import dataclass, field
from collections import defaultdict
import heapq

@dataclass
class Point:
    x: int
    y: int
    def __hash__(self):
        return hash((self.x, self.y))
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def __lt__(self, other):
        return self.x < other.x or (self.x == other.x and self.y < other.y)
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self


def main():
    x, y = map(int, input().split())
    p0_ = Point(x, y)
    x, y = map(int, input().split())
    p1_ = Point(x, y)

    DESK_SIZE = 8
    KNIGHT_MOVES = [
        Point(1, 2),
        Point(1, -2),
        Point(-1, 2),
        Point(-1, -2),
        Point(2, 1),
        Point(2, -1),
        Point(-2, 1),
        Point(-2, -1),
    ]

    MAX_DIST = 1000
    dist = defaultdict(lambda: MAX_DIST)
    move_ = 0
    dist[(p0_, p1_, move_)] = 0
    q = [(p0_, p1_, move_)]
    while q:
        p0, p1, move = q.pop(0)
        for delta in KNIGHT_MOVES:
            if move == 0:
                new_p0 = p0 + delta
                new_move = 1
                if 0 <= new_p0.x < DESK_SIZE and 0 <= new_p0.y < DESK_SIZE and new_p0 != p1:
                    new_p1 = p1
                    new_move = 1
                    if dist[(new_p0, new_p1, new_move)] == MAX_DIST:
                        dist[(new_p0, new_p1, new_move)] = dist[(p0, p1, move)] + 1
                        q.append((new_p0, new_p1, new_move))
            else:
                new_p1 = p1 + delta
                new_move = 0
                if 0 <= new_p1.x < DESK_SIZE and 0 <= new_p1.y < DESK_SIZE and new_p1 != p0:
                    new_p0 = p0
                    new_move = 0
                    if dist[(new_p0, new_p1, new_move)] == MAX_DIST:
                        dist[(new_p0, new_p1, new_move)] = dist[(p0, p1, move)] + 1
                        q.append((new_p0, new_p1, new_move))
    
    print(min(dist[(p1_, p0_, 0)], dist[(p1_, p0_, 1)]))
            
    
    
    

if __name__ == '__main__':
    main()
