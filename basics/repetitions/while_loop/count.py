print("How many live cables must I avoid?")
n = int(input())
x = 0
while (x < n):
  print(f"Avoiding... Done! {x + 1} live cables avoided.")
  x += 1
print("All live cables have been avoided.")