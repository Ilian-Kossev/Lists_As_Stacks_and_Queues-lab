expression = '1 + (3 + (4 + 5) + 6) + 7'
parentheses_indices = []

for index, ch in enumerate(expression):
    if ch == '(':
        parentheses_indices.append(index)
    elif ch == ')':
        closing_index = index
        opening_index = parentheses_indices.pop()
        print(expression[opening_index:closing_index + 1])

