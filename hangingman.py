stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', r'''
  +---+
  |   |
      |
      |
      |
      |
=========''']

word_list=['camel','baboon','Apple']
import random

chosen_word=random.choice(word_list)
print(chosen_word)

#1
placeholder=''
word_len=len(chosen_word)
for position in range(word_len):
    placeholder+='_'
print(placeholder)

game_over=False
correct_letter=[]
lives=6
while not game_over:
    guess=input('guess the letter: ').lower()
    display=''
    #2   
    for letter in chosen_word:
        if letter==guess:
            display+=letter    
            correct_letter.append(letter) 
        elif letter in correct_letter:
            display+=letter         
        else:
            display+='_'
    print(display)

    if guess not in chosen_word:
        lives-=1
        if lives==0:
            game_over=True
            print('you loos')
    
    if '_' not in display:
        game_over =True
        print('you won')

    print(stages[lives])
    
    

