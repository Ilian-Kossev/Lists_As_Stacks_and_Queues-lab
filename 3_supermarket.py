from collections import deque

queue = deque()
name = input()
while not name == 'end':
    if name == 'Paid':
        while queue:
            print(queue.popleft())
    else:
        queue.append(name)
    name = input()
print(f'{len(queue)} people remaining')











