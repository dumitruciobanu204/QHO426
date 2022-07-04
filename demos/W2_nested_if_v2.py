age = int(input("Enter age: "))
ch = int(input("Number of children: "))

if age > 25 and age <=55 and ch > 0: 
  print("You are a parent.")
  print(f"Next year you will be {age + 1} years old")
elif age > 55 and ch > 0:
  print("You should be a grandparent")
elif age < 18 or ch == 0:
  print("Don't worry, there is still time")
else: 
  print("Some other random text")