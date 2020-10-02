n = int(input('Enter the total numbers of 1 and 0: ')) + 1

for k in range(1, n):
    for i in range(1,n):
        j = i % 2
        if j != 0:
            print(0, end = ' ')
        else:
            print(1, end = ' ')

    print("")
