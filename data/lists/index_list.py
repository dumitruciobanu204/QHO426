def movements():
  path = ["Move Forward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1]
  return path

def run():
  print("Moving...")
  list = movements()
  
  i = 0
  
  while i < len(list):
    if list[i + 1] > 1:
      print(f"Moving {list[i]} for {list[i + 1]} steps")
    else: 
      print(f"Moving {list[i]} for {list[i + 1]} step")
      
    i = i + 2
      
run()