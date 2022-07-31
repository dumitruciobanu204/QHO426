def directions():
  directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
  return directions

def menu():
  print("Please select a direction: ")  
  dir = directions()
  n = 0
  while n < len(dir):
    print(f"{n}: {dir[n]}")
    n = n + 1
  index = int(input())
  return dir[index]

def run():
  print("Working out escape route...")
  route = []
  for i in range(5):
    route.append(menu())
  print(f"Escape route: {route}")
run()