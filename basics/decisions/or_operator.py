print("What type of adventure should I have?")
n = input()

if n.lower() == 'scary' or n.lower() == 'short':
  print("Entering the dark forest!")
elif n.lower() == 'safe' or n.lower() == 'long':
  print("Taking the safe route!")
else:
  print("Not sure which route to take.")