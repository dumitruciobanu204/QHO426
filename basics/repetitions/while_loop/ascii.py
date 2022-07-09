print("How many bars should be charged?")
n = int(input())
x = 0
while (x <= n):
  if x == 0:
    x += 1   
  print(f"Charging:", "\u275A" * x)
  x += 1
print("The battery is fully charged.")