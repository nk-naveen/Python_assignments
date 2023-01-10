def divisible(n):
    for i in range(1, n+1):
        if i % 5 == 0 and i % 7 == 0:
            yield i

n = int(input("enter a number: "))
    
div = []
for i in divisible(n):
    print(div.append(str(i)))
print(div)