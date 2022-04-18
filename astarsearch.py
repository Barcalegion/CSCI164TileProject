import tilegame as tg
import queue as q
import priorityqueue as pq

COST = 0
NODE_LIST = q.Queue()
NUM_EXPANDED = 0

class Node:
    
    def __init__(self,state,parent,action,cost):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost

    def print_node(self):
        tg.print_state(self.state)
        if(self.parent != "root"):
            print("parent node: " + self.parent.state)
        print("node action: " + self.action)

def a_star_search(problem):
    global COST
    global NODE_LIST
    global NUM_EXPANDED
    NUM_EXPANDED = 0
    node = Node(problem.initial,"root",None,0)
    frontier = pq.PriorityQueue()
    frontier.put(node,problem)
    reached = {problem.initial : node}
    
    while not is_empty(frontier):
        #frontier.print_queue()
        node = frontier.get()
        NUM_EXPANDED += 1
        if is_goal(node.state,problem):
            return node

        for child in expand(problem,node):
            if(child.action != "Illegal"):
                s = child.state
            
                if (s not in reached) or (child.cost < reached[s].cost):
                    reached[s] = child
                    frontier.put(child,problem)
                    NODE_LIST.put(child)
    return failed()

def is_empty(queue):
    if(queue.empty()):
        return True
    return False

def is_goal(state, problem):
    if(state == problem.goal):
        return True
    return False

def expand(problem, node):
    s = node.state
    for action in problem.actions(s): 
        if(tg.legal_move(s, action)== True):
            ss = tg.result(s,action)
            yield Node(ss,node,action,COST)
        else:
            yield Node(s,node,"Illegal",COST)

def failed():
    return False

