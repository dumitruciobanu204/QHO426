name = input("Enter your name: ")
nameLength = len(name)
if len(name) > 8:
  print("Too long! Enter your nickname: ")
  name = input()
elif len(name) <= 3:
  print("Too short!")
elif len(name) == "Dima":
  print("You are a champion!")
else:
  print(f"Welcome {name}!")
  