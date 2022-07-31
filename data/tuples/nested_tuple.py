def steps():
  likelihoods = [("step 2", 38),
                 ("step 3", 27),
                 ("step 4", 99),
                 ("step 5", 4)]
  return likelihoods

def run():
  n = steps()
  good_steps = []
  bad_steps = []
  
  for i in n:
    if i[1] <= 50:
      good_steps.append(i[0])
    else:
      bad_steps.append(i[0])
      
  print(f"Good steps: {good_steps}, Bad steps: {bad_steps}")

run()