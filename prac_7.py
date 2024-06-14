# Given a list of integer. You have to count and print the frequencies 
# of every integer
# Also print the number of unique elements in that list

list_int = [3, 4, 3, 0, 1]

count_dict = {}

for v in list_int:
  if v not in count_dict:
    count_dict[v] = 1
  else:
    count_dict[v] = count_dict[v] + 1

print(count_dict)

print(list(count_dict.keys()))