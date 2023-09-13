
# calculating using python: 
example_string = 'doesn\'t'
mult = 4 * 'asdf'
print(mult[-1:])

for i in range(9):
    print(i)


def fib(n):
    "docstring"
    # write fibonacci series up to n
    a, b = 0, 1
    while a<n:
        print(a)
        a, b = b, a+b
    print()


fib(15)