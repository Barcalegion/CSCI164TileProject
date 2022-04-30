import tilegame as tg
import queue as q

NODE_LIST = q.Queue()
NUM_EXPANDED = 0

class Node:
    
    def __init__(self,state,parent,action):
        self.state = state
        self.parent = parent
        self.action = action
        
    def print_node(self):
        tg.print_state(self.state)
        if(self.parent != "root"):
            print("parent node: " + self.parent.state)
        print("node action: " + self.action)

def breadth_first_search(problem):
    global NUM_EXPANDED
    NUM_EXPANDED = 0
    node = Node(problem.initial,"root","root")

    NODE_LIST.put(node)
    
    if(is_goal(node.state,problem)):
        return node

    frontier = q.Queue()
    frontier.put(node)
    reached = {problem.initial}

    while not is_empty(frontier):
        node = frontier.get()
        
        NUM_EXPANDED = NUM_EXPANDED + 1

        if(NUM_EXPANDED % 2000000) == 0:
            print("2 million nodes expanded")
    
        for child in expand(problem, node):
            
            if(child.action != "Illegal"):
                s = child.state
                
                if is_goal(s, problem):
                    NODE_LIST.put(child)
                    return child
                    
                if s not in reached:
                    reached.add(s)
                    frontier.put(child)
                    NODE_LIST.put(child)

    return failed()

def expand(problem, node):
    s = node.state
    for action in problem.actions(s):
        if(tg.legal_move(s, action)== True):
            ss = tg.result(s,action)
            yield Node(ss,node,action)
        else:
            yield Node(s,node,"Illegal")

def is_goal(state, problem):
    if(state == problem.goal):
        return True
    return False

def is_empty(queue):
    if(queue.empty()):
        return True
    return False

def failed():
    return print("BFS failed!")
    
