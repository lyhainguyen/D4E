initial = [0, 1]
for i in range(0, 5):
    next_month = initial[i] + initial[i+1]
    initial.append(next_month)
    print('MONTH', i, ':', next_month, 'pair(s) of rabbits')

