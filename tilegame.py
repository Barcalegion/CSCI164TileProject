import random
import heapq

random.seed(13)

InitialState = "123456078"
GoalState = "123456780"

StateDimension=3
Actions = lambda s: ['u', 'd', 'l', 'r']

def Result(state, action):
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

def PrintState(s):
  for i in range(0,len(s),StateDimension):
    print(s[i:i+StateDimension])

def LegalMove(state, action):
  i = state.index('0')
  row,col=i//StateDimension, i % StateDimension
  if ( (action=='u' and row==0) or
       (action=='d' and row==StateDimension-1) or
       (action=='l' and col==0) or
       (action=='r' and col==StateDimension-1)):
      return False
  return True
