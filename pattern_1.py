# n=3
# *
# **
# ***

n = 5
for i in range(n):
  for j in range(i+1):
    print('*', end = ' ')
  print()

# for i in range(1,n+1):
#   print('*'*i)