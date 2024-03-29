import tilegame as tg
import queue as q
import lifoqueue as lq

NODE_LIST = q.Queue()
NUM_EXPANDED = 0
DEPTH = 0

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
        
    def node_list(self):
        current_node = self
        
        sequence = []
        
        while current_node.parent != "root":
            parent = current_node.parent
            sequence.append(current_node.action)
            current_node = parent
                
        sequence.append(current_node.parent)
        
        reversed_list = sequence[::-1]
        
        return reversed_list
               
        def __lt__(self, other):
            return self.cost < other.cost

def depth_first_search(problem):
    global NUM_EXPANDED
    global DEPTH
    DEPTH = 0
    NUM_EXPANDED = 0
    count = 0
    
    node = Node(problem.initial,"root",None,DEPTH)
    NODE_LIST.put(node)
    
    if(is_goal(node.state,problem)):
        return node
        
    frontier = lq.LifoQueue()
    frontier.put(node)
    reached = {problem.initial}
    
    while not is_empty(frontier):
        
        if(count == 0):
            NUM_EXPANDED -= 1
            
        node = frontier.get()
        DEPTH += 1
        NUM_EXPANDED += 1
        count = 0
        
        if(NUM_EXPANDED >= 1000000):
            return False
        
        for child in expand(problem, node):
            if(child.action != "Illegal"):
                s = child.state
                if is_goal(s, problem):
                    NODE_LIST.put(child)
                    return child
                
                #without reached, dfs will enter a cycle
                if s not in reached:
                    count += 1
                    reached.add(s)
                    frontier.put(child)
                    NODE_LIST.put(child)
                    
    return failed()

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

def failed():
    return "DFS failed!"
    
