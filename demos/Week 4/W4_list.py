def adding(lista = []):
  new_member = input("Enter new avenger: ")
  lista.append(new_member)

def removing(lista = []):
  remove_member = input("Who to remove? ")
  if remove_member in lista:
    lista.remove(remove_member)
    print(f"{remove_member} has been removed!")

def printing(lista = []):
  for hero in lista:
    print(f"The mighty {hero} is part of the Avengers!")

def run():
  avengers = []
  while True:
    opt = int(input("Autobots, transform and roll out!\n 1. Add \n 2. Remove \n 3. Print \n 9. Exit "))
    if opt == 1:
      adding(avengers)
    elif opt == 2:
      if len(avengers) == 0:
        print("The list is empty!")
      else:
        removing(avengers)
    elif opt == 3:
      printing(avengers)
    elif opt == 9:
      break
    else: 
      print("Invalid input!")

run()