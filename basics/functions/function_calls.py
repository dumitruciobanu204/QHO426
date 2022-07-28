def box(word):
  x = len(word)
  if x <= 1:
    print(" -" * x)
    print("|{}|".format(word))
    print(" -" * x)
  else:
    print("- " * x)
    print("|{}|".format(word))
    print("- " * x)

def lower(word):
  print(word.lower())
  
def upper(word):
  print(word.upper())

def mirror(word):
  x = word[::-1]
  print(x)

def repeat(word):
  print("How many times to repeat?")
  x = int(input())
  print(f"{word} " * x)

def run():
  print("1. Display a box")
  print("2. Display Lower-case")
  print("3. Display Upper-case")
  print("4. Display Mirrored")
  print("5. Repeat")
  n = int(input())
  
  print("Enter a word: ")
  word = input()

  if n == 1:
    box(word)
  elif n == 2:
    lower(word)
  elif n == 3:
    upper(word)
  elif n == 4:
    mirror(word)
  elif n == 5:
    repeat(word)
  else:
    print("Try again!")

run()