direction = input("Towards which direction should I paint (up, down, left or right)? ")
if direction.lower() == 'up':
  print("I am painting in the upward direction!")
elif direction.lower() == 'down':
  print("I am painting in the downward direction!")
elif direction.lower() == 'left':
  print("I am painting in the left direction!")
elif direction.lower() == 'right':
  print("I am painting in the right direction!")
else: 
  print("I don't know such direction!")