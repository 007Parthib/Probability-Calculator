import copy
import random
#Consider using the modules imported above.

class Hat:
  def __init__(self, **x):
    contents = []
    for key in x.keys():
      for n in range(x[key]):
        contents.append(key)
    self.contents = contents
  
  def draw(self, num):
    contents = self.contents
    
    if num >= len(contents):
      return contents
    
    sample = []
    
    for i in range (num):
      len_contents = len(contents)
      index = random.randrange(len_contents)
      sample.append(contents[index])
      contents = contents[0:index] + contents[index+1:]
    
    self.contents=contents
    return sample

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  count=0
  for i in range (num_experiments):
    balls = copy.copy(hat)
    sample = balls.draw(num_balls_drawn)
    yes = True
    for key in expected_balls.keys():
      if sample.count(key) < expected_balls[key]:
        yes = False
        break
        
    if yes == True:
      count+=1
  
  return count/num_experiments

  
