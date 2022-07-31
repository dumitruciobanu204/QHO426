def directions():
  directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
  return directions

def menu():
  print("Please select a direction: ")
  n = directions()
  for i in range(len(n)):
    print(f"{i}: {n[i]}")

def run():
  menu()

run()