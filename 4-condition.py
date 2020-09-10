name = input('Enter your name: ')
print(f'my name is {name}')
#condition
userRank = int(input('what is your rank? '))

if userRank == 1:
    print('Gold')
elif userRank == 2:
    print('silver')
elif userRank == 3:
    print('bronze')
else:
    print('No! :)')
