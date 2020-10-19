initial_bacteria = int(input('How many B bacteria are there? '))
time = int(input('How much time in minutes will we wait? '))
total_bacteria = initial_bacteria*(2**(time/2))
print('After', time, 'minutes, we would have', total_bacteria, 'bacterias.')