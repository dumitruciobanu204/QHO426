import os
def cwd():
  path = os.getcwd()
  print(f"The current working directory is: {path}")
  print("The directory contains the following:")
  for i in os.listdir(path):
    print(i)

def run():
  print("Processing...")
  cwd()

run()