from collections import deque

kids_names_list = deque(input().split())
step = int(input())
counter = 0
while len(kids_names_list) > 1:
    counter += 1
    if counter == step:
        print(f'Removed {kids_names_list.popleft()}')
        counter = 0
    else:
        kids_names_list.append(kids_names_list.popleft())

print(f"Last is {''.join(kids_names_list)}")





