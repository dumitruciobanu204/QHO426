def t_area(b, h):
  area = b * h * 0.5
  print(area)
def run():
  print("Enter height")
  h = int(input())
  print("Enter base")
  b = int(input())
  print(t_area(b, h))

run()