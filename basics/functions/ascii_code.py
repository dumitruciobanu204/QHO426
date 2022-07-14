def ascii():
  print("Please enter a standard character:")
  n = input()
  if len(n) > 1:
    print("Error")
  else:
    value = ord(n)
    print(f"The value for {n} is {value}")
  
def run():
  print("Program started!")
  ascii()
  print("Program Ended!")

run()