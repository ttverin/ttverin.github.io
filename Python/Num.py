from random import randint

# Generates a number from 1 through 10 inclusive
random_number = randint(1, 10)
print(random_number)
guesses_left = 3
# Start your game!

while guesses_left > 0:
  guess = int(input("Your guess "))
  guesses_left = guesses_left - 1
  if guess == random_number:
    print ("You win!")
    break
  else:
    print ("Try again")
    print ("Guesses left "+str(guesses_left))

