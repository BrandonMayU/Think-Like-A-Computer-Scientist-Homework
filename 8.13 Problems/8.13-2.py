

def print_triangular_numbers(n):
    for i in range(1, n + 1):
        print("{0}          {1}".format(i, (i ** 2 + i)//2))

print_triangular_numbers(5)