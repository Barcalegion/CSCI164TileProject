import tilegame as tg
import queue as q
import priorityqueue as pq
import heapq as hq

COST = 0
NODE_LIST = q.Queue()
NUM_EXPANDED = 0

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


def a_star_search(problem):
    global COST
    global NODE_LIST
    global NUM_EXPANDED
    
    NUM_EXPANDED = 0
    
    node = Node(problem.initial,"root",None,0,problem)
    
    index = problem.initial
    minindex = index
    
    frontier = {}
    frontier[index] = node
    reached = {problem.initial : node}
    
    while len(frontier) != 0:
        #frontier.print_queue()
        minindex = min(frontier,key=frontier.get)
        node = frontier[minindex]
        del frontier[minindex]
        
        NUM_EXPANDED += 1
        if(NUM_EXPANDED >= 100000):
            return False
        
        if is_goal(node.state,problem):
            return node

        for child in expand(problem,node):
            if(child.action != "Illegal"):
                s = child.state
                if (s not in reached) or (child.cost < reached[s].cost):
                    reached[s] = child
                    frontier[s] = child
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
            yield Node(ss,node,action,0,problem)
        else:
            yield Node(s,node,"Illegal",0,problem)

def failed():
    return "A* failed!"
