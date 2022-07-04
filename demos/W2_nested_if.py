years = int(input("Enter number of years: "))
salary = float(input("Enter salary: "))

if years > 2:
  if salary < 25000:
    salary *= 1.1
    print(f"Your new salary is £{salary:.2f}")
  else: 
    salary += 100
    print(f"Your new salary is £{salary:.2f}")
elif years >=1:
  print("No salary incease for you Sir!")
else:
  if salary < 20000:
    print("Whoopsies! Your salary should be £20000")

print("\nTo space and beyond!")