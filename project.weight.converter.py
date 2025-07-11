weight = int(input('weight: '))
unit = input('(L)bs or (K)gs? ')
if unit.upper() == 'L':
    converted = int(weight) * 0.45
    print(f'You are {converted} kilos')
else:
    converted = int(weight) / 0.45
    print(f'You are {converted} pounds')