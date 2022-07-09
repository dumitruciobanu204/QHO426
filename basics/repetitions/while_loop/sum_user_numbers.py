print("How many numbers should I sum up?")
n = int(input())
x = 1
z = 0
while (x <= n):
  print(f"Please enter number {x} of {n}:")
  y = int(input())
  x += 1
  z = z + y
print(f"The answer is: {z}.")