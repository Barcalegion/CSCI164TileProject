import random
import heapq

random.seed(13)

StateDimension=3

class Problem:
  
  actions = lambda self, s: ['u', 'd', 'l', 'r']
  opposite = dict([('u','d'),('d','u'),('l','r'),('r','l'), (None, None)])
  
  def __init__(self,state,goal_state):
    self.initial = state
    self.goal = goal_state

  def get_init(self):
    return (self.initial, self.goal)
  
problems = []
problems.append(Problem("160273485","123456780"))
problems.append(Problem("462301587" ,"123456780"))
problems.append(Problem("821574360","123456780"))
problems.append(Problem("840156372","123456780"))
problems.append(Problem("530478126","123456780"))
problems.append(Problem("068314257","123456780"))
problems.append(Problem("453207186","123456780"))
problems.append(Problem("128307645","123456780"))
problems.append(Problem("035684712","123456780"))
problems.append(Problem("684317025","123456780"))
problems.append(Problem("028514637","123456780"))
problems.append(Problem("618273540","123456780"))
problems.append(Problem("042385671","123456780"))
problems.append(Problem("420385716","123456780"))
problems.append(Problem("054672813","123456780"))
problems.append(Problem("314572680","123456780"))
problems.append(Problem("637218045","123456780"))
problems.append(Problem("430621875","123456780"))
problems.append(Problem("158274036","123456780"))
problems.append(Problem("130458726","123456780"))

problems.append(Problem("16235A749C08DEBF","123456789ABCDEF0"))
problems.append(Problem("0634217859ABDEFC","123456789ABCDEF0"))
problems.append(Problem("012456379BC8DAEF","123456789ABCDEF0"))
problems.append( Problem("51246A38097BDEFC","123456789ABCDEF0"))
problems.append(Problem("12345678D9CFEBA0","123456789ABCDEF0"))

problems.append(Problem("71A92CE03DB4658F","123456789ABCDEF0"))
problems.append(Problem("02348697DF5A1EBC","123456789ABCDEF0"))
problems.append(Problem("39A1D0EC7BF86452","123456789ABCDEF0"))
problems.append(Problem("EAB480FC19D56237","123456789ABCDEF0"))
problems.append(Problem("7DB13C52F46E80A9","123456789ABCDEF0"))

problems.append(Problem("045372816","123456780"))
problems.append(Problem("721804356","123456780"))
problems.append(Problem("237416B8590CDAEF","123456789ABCDEF0"))
problems.append(Problem("132456879ABCDE0F","123456789ABCDEF0"))

"""
for x in range(30):
  print(problems[x].get_init(), x)
"""

def result(state, action):
  i = state.index('0')
  newState = list(state)
  row,col=i//StateDimension, i % StateDimension
  if ( (action=='u' and row==0) or
       (action=='d' and row==StateDimension-1) or
       (action=='l' and col==0) or
       (action=='r' and col==StateDimension-1)):
      return newState
  if action=='u':
    l,r = row*StateDimension+col, (row-1)*StateDimension+col
  elif action=='d':
    l,r = row*StateDimension+col, (row+1)*StateDimension+col
  elif action=='l':
    l,r = row*StateDimension+col, row*StateDimension+col-1
  elif action=='r' :
    l,r = row*StateDimension+col, row*StateDimension+col+1
  newState[l], newState[r] = newState[r], newState[l] 
  return ''.join(newState)

def legal_move(state, action):
  i = state.index('0')
  row,col=i//StateDimension, i % StateDimension
  if ( (action=='u' and row==0) or
       (action=='d' and row==StateDimension-1) or
       (action=='l' and col==0) or
       (action=='r' and col==StateDimension-1)):
      return False
  return True

def out_of_place(left, right):
  distances = [left[i]!=right[i] and right[i] != '0'
     for i in range(StateDimension**2)]
  return sum(distances)

def single_tile_manhattan_distance(tile, left, right):
  leftIndex = left.index(tile)
  rightIndex = right.index(tile)
  return (abs(leftIndex//StateDimension-rightIndex//StateDimension) +
          abs(leftIndex%StateDimension-rightIndex%StateDimension))

def manhattan_distance(left, right):
  distances = [single_tile_manhattan_distance(tile, left, right) 
    for tile in [str(c) for c in range(1, StateDimension**2)]]
  ### print ("Distances= ", distances)
  return sum(distances)

def print_state(s):
  print("\n") 
  print("node state: ")
  for i in range(0,len(s),StateDimension):
    print(s[i:i+StateDimension])
