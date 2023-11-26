from dataclasses import dataclass, field
from enum import IntEnum

class Type(IntEnum):
    START = 1
    END = 2

@dataclass(order=True)
class Event:
    x: int
    type: Type 
    low: int = field(compare=False)
    high: int = field(compare=False)

    def __eq__(self, __value: object) -> bool:
        return self.low == __value.low and self.high == __value.high and self.type == __value.type

@dataclass(order=True, eq=True)
class Point:
    x: int
    type: Type


class SortedPointsList:
    def __init__(self):
        self._data = []
    
    def add(self, point: Point):
        self._data.append(point)
        point_id = len(self._data) - 1
        while point_id > 0:
            if self._data[point_id] < self._data[point_id - 1]:
                self._data[point_id], self._data[point_id - 1] = self._data[point_id - 1], self._data[point_id]
                point_id -= 1
            else:
                break

    def get_coverage(self):
        if not self._data:
            return 0
        
        coverage = 0
        open_count = 0
        prev_x = self._data[0].x
        for point in self._data:
            coverage += int(open_count > 0) * (point.x - prev_x)
            prev_x = point.x
            open_count += 1 if point.type == Type.START else -1
        return coverage

    def remove(self, point: Point):
        self._data.remove(point)

    def __get_item__(self, index):
        return self._data[index]
    
    def __bool__(self):
        return bool(self._data)
    
    def __len__(self):
        return len(self._data)




def main():
    n = int(input())
    events = []
    for _ in range(n):
        start, low, end, high = map(int, input().split())
        events.append(Event(start, Type.START, low, high))
        events.append(Event(end, Type.END, low, high))
    events.sort()

    points = SortedPointsList()
    coor_x = events[0].x
    union_area = 0
    for ev in events:
        union_area += points.get_coverage() * (ev.x - coor_x)
        coor_x = ev.x
        if ev.type == Type.START:
            points.add(Point(ev.low, Type.START))
            points.add(Point(ev.high, Type.END))
        else:
            points.remove(Point(ev.low, Type.START))
            points.remove(Point(ev.high, Type.END))

    print(union_area)
        

if __name__ == '__main__':
    main()