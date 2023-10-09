# The Collatz Sequence

def collatz(number):
    if number%2==0:
        coll = number // 2 
        print(coll)
        return coll
    elif number%2 != 0:
        coll = 3* number + 1
        print(coll)
        return coll
    

def input_loop():
    result = int(input())
    while result != 1:
        result = collatz(result)

input_loop()
        
