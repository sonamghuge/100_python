import random
letter=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',' A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
number=['1','2','3','4','5','6','7','8','9']
symbol=['@','!','$','%','^','&','*','(',')']
print('welcome to the password genrator')

l= int(input('How many letter  would you like in your password?'))
s=int(input('how many symbol would you like?'))
n=int(input('How manu number would you like?'))

password=''

for char in range(0,l):
    password+=random.choice(letter)
    # print(password)

for sys in range(0,s):
    password+=random.choice(symbol)

for num in range(0,n):
    password+=random.choice(number)

print(password)
