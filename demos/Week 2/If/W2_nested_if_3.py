h = input("Are you happy? Y/N ")
k = input("Do you know it? Y/N ")

if h.upper == 'Y' and k.upper() == 'Y':
  print("boop")
elif h.upper() == 'N' and k.upper() == 'N':
  print("boop beep")
elif h.upper() == 'N':
  print("boop beep boop")
elif k.upper() == 'Y':
  print("boop beep boop beep")
else:
  print("boop beep boop beep boop ?")