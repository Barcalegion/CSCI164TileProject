import enum
import tilegame as tg
"""
class Actions(enum.Enum):
    u = 0
    d = 1
    l = 2
    r = 3
    root = 4
"""
class PriorityQueue(object):
    
    def __init__(self):
        self.queue = []
        
    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    def empty(self):
        return len(self.queue) == 0

    def put(self,node,problem):
        evaluation_function(node,problem)
        self.queue.append(node)
        
        
    def len(self):
        return len(self.queue)
    
    def print_queue(self):
        print()
        for x in range(len(self.queue)):
            print("state: ", self.queue[x].state,"action: ",self.queue[x].action, " cost: ",self.queue[x].cost)

    def get(self):
        minimum = 10000000
        index = 0
        for i in range(len(self.queue)):
            if self.queue[i].cost < minimum:
                minimum = self.queue[i].cost 
                item = self.queue[i]
                index = i
        del self.queue[index]
        return item

#choose a hueristic function down here!!!
def evaluation_function(node,problem):
    if node.parent != "root":
        current_node = node
        
        while node.parent != "root":
            parent = node.parent
            current_node.cost = current_node.cost+1
            node = parent
            
        g = current_node.cost
        #choose a heuristic function
        #h = tg.out_of_place(current_node.state,problem.goal)
        h = tg.manhattan_distance(current_node.state,problem.goal)
        f = g + h
    
        current_node.cost = f
