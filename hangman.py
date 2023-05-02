# HANGMAN GAME
import os

print('Lets play hangman!')
word = input('Enter a word for your friend to guess: ')
word = word.lower()
# used to clear the screen
os.system('clear')

def hangman(word):
  str1 = ''
  trys = len(word)
  print(f'You have {trys} guesses')
  
  # creates visual blank word for person to guess
  for i in range(0,len(word) ):
    str1 += '_'
    
  while word != str1 and trys > 0:
    counter = 0
    print(str1)
    guess = input('Guess a letter: ')
    guess = guess.lower()
    for i in range(0,len(word)):
        if guess == word[i]:
            str1 = str1[:i] + guess + str1[i+1:]
            counter += 1
        
    if counter >= 1 :
        print(f"\n{guess} was in the word!")
    else:
        trys -= 1
        print(f"\nSorry '{guess}' was not in the word :( \nYou have {trys} trys left")
    
  if word == str1 and trys > 0:
    return f'Congrats You have guessed {word} correctly!'
  else:
    return f'Sorry You ran out of trys :/  \nThe word was {word} '
print(hangman(word))
