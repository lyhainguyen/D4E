n = int(input('Enter a number: ')) + 1
j = 0

for i in range(1, n):
    j += 1
    for k in range(1, n):
        print(k * i, end= " ")
    print("")
