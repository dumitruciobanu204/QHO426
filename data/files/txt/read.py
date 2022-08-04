def search(n):
  print("Searching...")
  with open(n) as file:
    for i in file.readlines():
      print(f"Looked in: {i.strip()}")
  print("...Done!")

def run():
  search("data/files/txt/locations.txt")

run()