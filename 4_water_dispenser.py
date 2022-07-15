from collections import deque

queue = deque()
dispenser_litres = int(input())
name = input()
while not name == 'Start':
    queue.append(name)
    name = input()

command = input()
while not command == 'End':
    if command.startswith('refill'):
        litres_to_refill = int(command.split()[-1])
        dispenser_litres += litres_to_refill
    else:
        needed_litres = int(command)
        if dispenser_litres >= needed_litres:
            print(f'{queue.popleft()} got water')
            dispenser_litres -= needed_litres
        else:
            print(f'{queue.popleft()} must wait')
    command = input()
print(f'{dispenser_litres} liters left')
