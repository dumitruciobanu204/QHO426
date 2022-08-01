def observed():
  observations = []
  for i in range(5):
    print("Please enter an observation:")
    observations.append(input())
  return observations

def remove_observations(observations):
  x = True
  while x:
    print("Do you wish to remove an observation (yes/no)?")
    n = input()
    if n == 'yes':
      print("What observation you wish to remove")
      m = input()
      observations.remove(m)
      print("Done!")
    else:
      x = False

def run():
  x = observed()
  remove_observations(x)
  m = set()
  for i in x:
    a = (i, x.count(i))
    m.add(a)
  for i in m:
    print(f"{i[0]} observed {i[1]} times.")

run()