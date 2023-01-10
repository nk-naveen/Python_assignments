class reverse(object):
    def __init__(self, my_list):
        self.index = -1
        self.my_list = my_list

    def __iter__(self):
        return self

    def __next__(self):
        try:
            result = self.my_list[self.index]
        except IndexError:
            self.my_list = [] 
            raise StopIteration
        self.index -= 1
        return result


for i in reverse([1,2,3,4,5,6,8,9,7]):
    print(i)

print("------")

for i in reverse(["red", "blue", "green"]):    
    print(i)
