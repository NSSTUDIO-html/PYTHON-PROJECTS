rows = 5

# Roof (Triangle)
for i in range(1, rows + 1):
    print(' ' * (rows - i) + '*' * (2 * i - 1))

# Walls (Rectangle)
for i in range(rows):
    print('*' + ' ' * (2 * rows - 3) + '*')

# Land (Rectangle)
for i in range(1):
    print('*' * 9)