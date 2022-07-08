n = input("Where should I look? ")

if n.lower() == 'in the bedroom' or n.lower() == 'in the bathroom' or n.lower() == 'in the lab':
  if n.lower() == 'in the bedroom':
    n = input("Where in the bedroom should I look? ")
    if n.lower() == 'under the bed':
      print("Found some shoes but no battery")
    else:
      print("Found some mess but no battery")
  
  if n.lower() == 'in the bathroom':
    n = input("Where in the bathroom should I look? ")
    if n.lower() == 'in the bathtub':
      print("Found a rubber duck but no battery")
    else:
      print("Found a wet surface but no battery")
  
  if n.lower() == 'in the lab':
    n = input("Where in the lab should I look? ")
    if n.lower() == 'on the table':
      print("Yes! I found my battery!")
    else:
      print("Found some tools but no battery.")
else:
  print("I do not know where that is but I will keep looking.")