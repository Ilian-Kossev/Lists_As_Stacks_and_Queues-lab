from collections import deque

kids_names_list = deque(input().split())
step = int(input())
counter = 0
while len(kids_names_list) > 1:
    counter += 1
    kids_names_list.rotate(-1)
    if counter == step:
        print(f'Removed {kids_names_list.pop()}')
        counter = 0
print(f"Last is {''.join(kids_names_list)}")

