n = input("What type of cover does the book have? ")
if n.lower() == 'soft':
  n = input("Is the book perfect-bound? ")
  if n.lower() == 'yes':
    print("Soft cover, perfect bound books are very popular!")
  else:
    print("Soft covers with coils or stitches are great for short books")
elif n.lower() == 'hard':
  print("Books with hard covers can be more expensive! ")