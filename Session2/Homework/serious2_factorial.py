n = int(input('Enter an integer number: '))

while True:
    factorial = 1
    for i in range(1, n+1):
        factorial = factorial*i
    break
print('Factorial of',(n) ,'is: ', factorial)