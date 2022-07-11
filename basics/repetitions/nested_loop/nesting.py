print("Please enter a sequence")
seq = input()
print("\nPlease enter the character for the marker")
marker = input()
pos1 = -1
pos2 = -1

for i in range(0, len(seq)):
    if (seq[i] == marker):
      if pos1 == -1:
        pos1 = i
      else:
        pos2 = i
print(f"\nThe distance between the markers is: {pos2 - pos1 - 1}")