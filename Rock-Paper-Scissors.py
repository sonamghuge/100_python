import random

rock= '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper= '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
sessior='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images=[rock,paper,sessior]

user_choice=int(input('what do you choes? Type 0 Rock , 1 for paper or 2 for Scissors\n'))
if user_choice>=0 and user_choice<=2:
    print(game_images[user_choice])

computer_choic=random.randint(0,2)
print('computer choice')
print(game_images[computer_choic])

if user_choice>=3 or user_choice<0:
    print('Invlid num')
elif (user_choice==0 and computer_choic==2):
    print('you win!')
elif(computer_choic==0 and user_choice==2):
    print('you loos!')
elif (computer_choic>user_choice):
    print('you loos!')
elif(computer_choic==user_choice):
    print('its draw')
elif(user_choice>computer_choic):
    print('you win')
elif user_choice>=3 or user_choice<0:
    print('Invlid num')



