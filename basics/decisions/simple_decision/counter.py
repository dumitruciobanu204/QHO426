n1 = int(input("Please enter the first whole number. "))
n2 = int(input("Please enter the second whole number. "))
n3 = int(input("Please enter the third whole number. "))
even_counter = 0
odd_counter = 0

if n1 % 2 == 0:
  even_counter +=1
else:
  odd_counter +=1
  
if n2 % 2 == 0:
  even_counter +=1
else:
  odd_counter +=1

if n2 % 2 == 0:
  even_counter +=1
else:
  odd_counter +=1
  
print(f"There are {even_counter} even and {odd_counter} odd number")