def fib(n):
    if n<=1:
        return n
    else:
        return(fib(n-1)+fib(n-2))
num=int(input('enter the numbers:'))
if num<=0:
    print('enter valid number')
else:
    print('fibonacci series:')
    for i in range(num):
        print(fib(i))
