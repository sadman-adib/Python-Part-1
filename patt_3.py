# n=3
#   *
#  **
# ***

n = 5

for i in range(n):
    print(' ' * (n - i - 1), end=' ')
    print('*' * (i + 1))