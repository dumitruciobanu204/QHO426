print("What strange markings do you see?")
n = input()
print("\nIdentifying...\n")
for i in range(0, len(n), 1):
  print(f"index {i}:", n[i])
print("\nDone!")