def observed():
  observations = []
  for i in range(7):
    print("Please enter an observation:")
    observations.append(input())
  return observations

def run():
  print("Counting observations...")
  n = observed()
  m = set()
  for i in n:
    x = (i, n.count(i))
    m.add(x)

  for x in m:
    print(f"{x[0]} observed {x[1]} times.")

run()