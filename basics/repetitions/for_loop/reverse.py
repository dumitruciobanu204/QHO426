print("What phrase do you see?")
n = input()
x = ""
print("\nReversing...")
for i in n:
  x = i + x
print("\nThe phrase is: ", end="")
print(x)