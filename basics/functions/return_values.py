def sum_weight(weight_beep, weight_boop):
  sum = weight_beep + weight_boop
  return sum

def calc_avg_weight(weight_beep ,weight_boop):
  avg = weight_beep + weight_boop % 2
  return avg

def run():
  print("What is the weight of Beep?")
  weight_beep = float(input())
  print("What is the weight of Boop?")
  weight_boop = float(input())
  print("What would you like to calculate(sum or average)?")
  n = input()
  if n == 'sum':
    x = sum_weight(weight_beep, weight_boop)
    if x // 1 == x / 1:
      print(f"The sum of Beep's and Bop's wight is {x:.0f}")
    else:
      print(f"The sum of Beep's and Bop's wight is {x:.2f}")
  elif n == 'average':
    x = calc_avg_weight(weight_beep, weight_boop)
    if x // 1 == x /1:
      print(f"The average weight of Beep and Bop is {x:.0f}")
    else: 
      print(f"The average weight of Beep and Bop is {x:.2f}")
run()