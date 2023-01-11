my_list = [12,24,74,585,999,35,24,88,120,155,88,120,155]

print("list with duplicatses" + str(my_list))

my_list1 = list(set(my_list))

my_list1.sort(key=my_list.index)

print("list without duplicates" + str(my_list1))


