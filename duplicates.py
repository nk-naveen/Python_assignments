my_list = [12,24,35,24,88,120,155,88,120,155]

print("list with duplicatses" + str(my_list))

my_list = list(set(my_list))

my_list.sort()
print("list without duplicates" + str(my_list))

