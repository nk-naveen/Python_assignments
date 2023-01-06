
n = input ("enter a number: ")
    
divisible(n)
    
def divisible(n):
    for i in range(1,n+1):
        if i % 5 == 0 or i % 7 == 0:
            yield i
            print(i)

