def likelihood():
  likelihoods = (50, 38, 27, 99, 4)
  return min(likelihoods), max(likelihoods)

def run():
  n = likelihood()
  print(f"Maximum likelihood of falling: {max(n)}%")
  print(f"Minimum likelihood of falling: {min(n)}%")

run()