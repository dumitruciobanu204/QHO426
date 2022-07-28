import random
print("Please enter the minimum value:")
min = int(input())
print("Please enter the maximum value:")
max = int(input())
random = random.randint(min, max)
print(f"I am thinking of a number betweer {min} and {max}. Can you guess what it is?")
n = 0

while n != random:
  print("Enter a number:")
  n = int(input())

  if n < random:
    print("Your guess is too low!\nTry again!")
  elif n > random:
    print("Your guess is too high!\nTry again!")
  else:
    print("Congratulations! You guessed my number!")