from collections import deque

potatoes = input().split(' ')
potatoes_queue = deque()
step = int(input())

for p in potatoes:
    potatoes_queue.appendleft(p)

while potatoes_queue:
    for _ in range(step - 1):
        potatoes_queue.appendleft(potatoes_queue.pop())