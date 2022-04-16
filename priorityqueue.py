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
  
    def put(self,node):
        self.queue.append(node)
        
    def len(self):
        return len(self.queue)

    def action(self):
        for x in range(len(self.queue)):
            print(self.queue[x].action, " depth: ",self.queue[x].depth)
    
    def get(self):
        
        depth = 0
        
        if self.queue[0].action == "root":
            item = self.queue[0]
            depth = self.queue[0].depth
            del self.queue[0]
            print("node being selected ", item.state, "action: ", item.action, "depth: ", item.depth)
            return item
        else:
            depth = self.queue[-1].depth
            item = self.queue[-1]
            
        del self.queue[-1]
                           
        print("node being selected ", item.state, "action: ", item.action, "depth: ", item.depth)
            
        return item
        """
        if self.queue[0][2] == "root":
            item = self.queue[0][0]
            del self.queue[0]
            print("This should only happen once! ", item)
            return item
        else:
            
            max_depth = 0
            same_depth = []
            action_priority = []
            action_taken = 0
            depth = 1
            
            #print(self.queue)
                #find the index of the deepest node
            for i in range(len(self.queue)):
                if self.queue[i][1] > self.queue[max_depth][1]:
                    max_depth = i
                    depth = self.queue[i][1]
            
            #print(self.queue[i][1])
                #store all the nodes that are the deepest (u,d,l,r) 
            for i in range(len(self.queue)):
                if self.queue[i][1] == depth:
                    same_depth.append(self.queue[i])
                    
            #print(same_depth)
                #give int values to actions (u,d,l,r)
            for x in range(len(same_depth)):
                if same_depth[x][2] == 'u':
                    action_priority.append(0)
                elif same_depth[x][2] == 'd':
                    action_priority.append(1)
                elif same_depth[x][2] == 'l':
                    action_priority.append(2)
                elif same_depth[x][2] == 'r':
                    action_priority.append(3)
                else:
                    action_priority.append(4)
           
                #choose the lowest action due to its value
            if(len(action_priority) != 0):
                action_taken = min(action_priority)
                
            print(action_priority)
            
                #if action is illegal remove action and check for next priority action
            while tg.legal_move(self.queue[0][0].state, action_taken)== False:
                action_priority.remove(min(action_priority))
                action_taken = min(action_priority)
         
                #set return value to node of the legal action being taken.    
            for x in range(len(same_depth)):
                if Actions(action_taken).name in same_depth[x][2]:
                    item = same_depth[x][0]

            action_taken = 0
            del action_priority
            del same_depth
            max_depth = 0
            """
            
