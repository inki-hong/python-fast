state = '123405678'

nested_list = []

# c = state[0]
# print(c)
# c = state[1]
# print(c)
# ...

for index, c in enumerate(state):
    print(index, c)
    if index % 3 == 0:
        inner_list = []
        nested_list.append(inner_list)
        inner_list.append(c)
    else:
        inner_list = nested_list[index // 3]
        inner_list.append(c)

# print(nested_list)

for row in nested_list:
    print(row)

pos_zero = None
for r, row in enumerate(nested_list):
    for c, col in enumerate(row):
        if nested_list[r][c] == '0':
            pos_zero = (r, c)


pos_zero = (1, 1)  # calculate this from code

move = 'UP'
if move == 'UP':
    row = pos_zero[0]
    col = pos_zero[1]
