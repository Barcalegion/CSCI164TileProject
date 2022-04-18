import tilegame as tg
import queue as q
import lifoqueue as lq
import itertools

NODE_LIST = q.Queue()
NUM_EXPANDED = 0
DEPTH = 0
CUTOFF = 0

class Node:
    
    def __init__(self,state,parent,action,depth):
        self.state = state
        self.parent = parent
        self.action = action
        self.depth = depth
        
    def print_node(self):
        tg.print_state(self.state)
        if(self.parent != "root"):
            print("parent node: " + self.parent.state)
        print("node action: " + self.action)

def iterative_deepening_search(problem):
    
    for depth in itertools.count():
        
        result = depth_limited_search(problem, depth)

        if result != CUTOFF:
            return result

def depth_limited_search(problem, limit):
    global DEPTH
    global CUTOFF
    global NUM_EXPANDED

    NUM_EXPANDED = 0
    DEPTH = 0
    frontier = lq.LifoQueue()
    frontier.put(Node(problem.initial,"root",None,DEPTH))
    result = failed()
    
    while not is_empty(frontier):
        node = frontier.get()
        NUM_EXPANDED += 1
        if(is_goal(node.state,problem)):
            return node
        #depth(node)
        if node.depth >= limit or (node.depth == 0 and limit == 0):
            CUTOFF = node.depth
            result = CUTOFF
        elif not is_cycle(node):
            #DEPTH += 1
            for child in expand(problem, node):
                if(child.action != "Illegal"):
                    child.depth = depth(child)
                    frontier.put(child)
                    NODE_LIST.put(child)
    return result

def expand(problem, node):
    s = node.state
    for action in problem.actions(s): 
        if(tg.legal_move(s, action)== True):
            ss = tg.result(s,action)
            yield Node(ss,node,action,DEPTH)
        else:
            yield Node(s,node,"Illegal",DEPTH)

def is_goal(state, problem):
    if(state == problem.goal):
        return True
    return False

def is_empty(queue):
    if(queue.empty()):
        return True
    return False

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

def depth(node):
    d = 0
    while node.parent != "root":
        parent = node.parent
        node = parent
        d += 1
    return d

def failed():
    return False
    
