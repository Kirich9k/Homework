def print_operation_table(operation, a, b):
    for i in range(1, a + 1):
        for j in range(1, b + 1):
            print(f'{operation(i, j) : 4}', end = ' ')
        print()
num_rows = 6
num_columns  = 6
print_operation_table(lambda x, y: x * y, num_rows, num_columns)