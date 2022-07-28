def generate():
  name = input("Enter name: ")
  mrk = int(input("Enter final mark: "))
  return name, mrk

def student_list(n):
  list = []
  for i in range(n):
    list.append(generate())
  return list

def avg_mrk(list = []):
  total = 0
  for tup in list:
    total += tup[1]
  average = total / len(list) 
  return average

def run():
  stud_list = []
  while True:
    opt = int(input("Menu:\n 1. Populate list of students\n 2. Calculate average mark\n 3. Change mark of a student\n 4. Print student list with marks\n 5. Exit\nOption: "))
    if opt == 1:
      print("Enter number of students")
      num = int(input())
      stud_list.extend(student_list(num))
    elif opt == 2:
      if len(stud_list) == 0:
        print("List is empty!")
      else:
        print(f"The average is: {avg_mrk(stud_list):.0f}")
    elif opt == 3:
      if len(stud_list) == 0:
        print("List is empty!")
      else:
        name = input("Enter name of student: ")
        for student in stud_list:
          if student[0].lower() == name.lower():
            n_mrk = int(input(f"Enter mark for {name}:"))
            stud_list.remove(student)
            stud_list.insert(0, (name, n_mrk))
    elif opt == 4:
      if len(stud_list) == 0:
        print("Empty list!")
      else:
        print(f"{stud_list}")
    elif opt == 5:
      break
      
run()      