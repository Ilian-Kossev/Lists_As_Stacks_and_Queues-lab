string = input().split()
stack = []
while string:
    stack.append(string.pop())
print(' '.join(stack))


s = 'I love Python'
ss = []
for ch in s:
    ss.append(ch)

result = ''
while len(ss) > 0:
    result += ss.pop()

print(result)


