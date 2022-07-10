print("How many rows would like?")
x = int(input())
print("How many columns would you like?")
y = int(input())
print("Here I go:")
for i in range(0, x, 1):
  for i in range(0, y, 1):
    print("\u270C ", end="")
  print()