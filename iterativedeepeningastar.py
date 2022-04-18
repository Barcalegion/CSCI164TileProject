import tilegame as tg
import queue as q
import priorityqueue as pq

COST = 0
NODE_LIST = q.Queue()
NUM_EXPANDED = 0
CUTOFF = 0

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

def iterative_deepening_a_star_search(problem):

    while True:
        
        result = iterative_deepening_search(problem, COST)

        if result != CUTOFF:
            return result

def iterative_deepening_search(problem,limit):
    global COST
    global NODE_LIST
    global NUM_EXPANDED
    
    COST = 0 
    NUM_EXPANDED = 0
    
    node = Node(problem.initial,"root",None,0)
    frontier = pq.PriorityQueue()
    frontier.put(node,problem)
    
    #reached = {problem.initial : node}
    
    while not is_empty(frontier):
        frontier.print_queue()
        
        node = frontier.get()
        
        NUM_EXPANDED += 1
        
        if is_goal(node.state,problem):
            return node
        
        if node.cost >= limit or node.cost == 0 and limit == 0:
            CUTOFF = node.cost
            result = CUTOFF
        #elif not is_cycle(node):
        else:
            for child in expand(problem,node):
                if(child.action != "Illegal"):
                    frontier.put(child,problem)
                    NODE_LIST.put(child)
                #if (s not in reached) or (child.cost < reached[s].cost):
                    #reached[s] = child
                    
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
            yield Node(ss,node,action,0)
        else:
            yield Node(s,node,"Illegal",0)
            
def is_cycle(node):
    
    current_node = node
    cycle = False

    if node.parent == "root":
        cycle = False
    else:
        while node.parent != "root":
            parent = node.parent
            if current_node.state == parent.state:
                cycle = True
            node = parent
    return cycle

def failed():
    return False

