print('Welcome to the tip calculator!')
bill = float(input('what was the total bill? rs'))
tip= int(input("home much tip you like to give> 10 ,20  or 15? "))
person= int(input("how many people to spilt the bill? "))
how= (tip/100*bill+bill)/person
print(f'Each person shold pay: rs{how}')