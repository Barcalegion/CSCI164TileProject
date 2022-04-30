import tilegame as tg
import queue as q
import priorityqueue as pq

COST = 0
NODE_LIST = q.Queue()
NUM_EXPANDED = 0
CUTOFF = 0
STORE_NUM_EXPANDED = 0

def evaluation_function(node,problem):
        if node.parent != "root":
    
            current_node = node
        
            while node.parent != "root":
                parent = node.parent
                current_node.cost = current_node.cost+1
                node = parent

            #choose a heuristic function
            #h = tg.out_of_place(current_node.state,problem.goal)
            g = current_node.cost
            h = tg.manhattan_distance(current_node.state,problem.goal)
            f = g + h
            current_node.cost = f
        else:
            node.cost = 0
            
class Node:
    
    def __init__(self,state,parent,action,cost,problem):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost
        self.problem = None
        evaluation_function(self,problem)
        
    def print_node(self):
        tg.print_state(self.state)
        if(self.parent != "root"):
            print("parent node: " + self.parent.state)
        print("node action: " + self.action)

def iterative_deepening_a_star_search(problem):
    global COST
    global STORE_NUM_EXPANDED

    COST = tg.manhattan_distance(problem.initial,problem.goal)
    
    STORE_NUM_EXPANDED = 0
    
    while True:
        
        result = iterative_deepening_search(problem, COST)
        
        if(result == None):
            return False
        
        if result != CUTOFF:
            return result

def iterative_deepening_search(problem,limit):
    global COST
    global NODE_LIST
    global NUM_EXPANDED
    global CUTOFF
    global STORE_NUM_EXPANDED
    
    
    print(STORE_NUM_EXPANDED)
    NUM_EXPANDED = 0
    
    node = Node(problem.initial,"root",None,0,problem)
    frontier = pq.PriorityQueue()
    frontier.put(node)
    
    while not is_empty(frontier):
        
        node = frontier.get()
        
        NUM_EXPANDED += 1
        
        STORE_NUM_EXPANDED += 1
        
        if(STORE_NUM_EXPANDED >= 100000):
            return None
        
        if is_goal(node.state,problem):
            return node
        
        if node.cost > limit:
        
            CUTOFF = node.cost
            COST = node.cost
            result = CUTOFF
    
        else:
            for child in expand(problem,node):
                if(child.action != "Illegal"):
                    frontier.put(child)
                    NODE_LIST.put(child)
                     
    return result

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
            yield Node(ss,node,action,0,problem)
        else:
            yield Node(s,node,"Illegal",0,problem)
            

def failed():
    return False

