full_name = input(str('Your full name: '))
full_name = full_name.lower()
standard = full_name.split()

for i in range(len(standard)):
    standard[i] = standard[i].capitalize()
updated = ' '.join(standard)

print('Updated: ', updated)
