from dataclasses import dataclass, field

@dataclass
class Train:
    x: int = field(default=0)
    block_id: int = field(default=0)
    time_in_block: int = field(default=0)

@dataclass
class Block:
    velocity: int
    time: int
    start: int
    end: int = field(init=False)

    def __post_init__(self):
        self.end = self.start + self.velocity * self.time


def move(blocks, train, time):
    cur_block = blocks[train.block_id]
    time_left = cur_block.time - train.time_in_block
    if time < time_left:
        train.x += time * cur_block.velocity
        train.time_in_block += time
        return
    
    train.x += time_left * cur_block.velocity
    train.time_in_block = 0
    train.block_id += 1
    if train.block_id < len(blocks):
        move(blocks, train, time - time_left)

def check_distance(train1, train2):
    return train1.x - train2.x >= MIN_DISTANCE_BETWEEN

def check(blocks, T):
    train1, train2 = Train(), Train()
    move(blocks, train1, T)
    if not check_distance(train1, train2):
        return False
    
    while train1.block_id < len(blocks):
        time1_to_next = blocks[train1.block_id].time - train1.time_in_block
        time2_to_next = blocks[train2.block_id].time - train2.time_in_block
        time_to_next = min(time1_to_next, time2_to_next)
        move(blocks, train1, time_to_next)
        move(blocks, train2, time_to_next)
        if not check_distance(train1, train2):
            return False
    
    return True



def main():
    global MIN_DISTANCE_BETWEEN
    MIN_DISTANCE_BETWEEN = int(input())
    n_blocks = int(input())
    blocks = []
    current_x = 0
    for _ in range(n_blocks):
        time, velocity = map(int, input().split())
        blocks.append(Block(velocity, time, current_x))
        current_x += velocity * time

    left, right = 0, 10**6
    eps = 10**(-6)
    while right - left > eps:
        middle = (left + right) / 2
        if check(blocks, middle):
            right = middle
        else:
            left = middle
    
    print(right)
        

if __name__ == '__main__':
    main()