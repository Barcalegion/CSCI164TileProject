import tilegame as tg
import breadthfirstsearch as bfs
import depthfirstsearch as dfs

"""
function to get the sequence for the solution of the puzzle.
argument is a queue that contains all the nodes reached.
"""
def solution(nodes):
    node_list = nodes
    node = []
    i = 0
    while not nodes.empty():
        node.append(nodes.get())
        node_state = node[i].state
        i = i + 1
    
    goal_child = node[-1]
    sequence = []
    current_node = goal_child
    sequence.append(current_node.action)

    while current_node.parent != "root":
       parent = current_node.parent
       sequence.append(parent.action)
       current_node = parent

    reversed_list = sequence[::-1]

    return reversed_list

#breadth first search
for i in range(30):
    if i == 20:
        tg.StateDimension = 4
    print("PROBLEM: ", i, " ", tg.problems[i].initial)
    bfs.breadth_first_search(tg.problems[i])
    print("Sequence to find solution: ", solution(bfs.NODE_LIST))
    print("Number of expanded nodes to find solution: ", bfs.NUM_EXPANDED, "\n")

#depth first search
for i in range(30):
    if i == 20:
        tg.StateDimension = 4
    print("PROBLEM: ", i)
    print(dfs.depth_first_search(tg.problems[i]))
    print("Sequence to find solution: ", solution(dfs.NODE_LIST))
    print("Number of expanded nodes to find solution: ", dfs.NUM_EXPANDED, "\n")


"""
print("Problem 1")
#dfs.depth_first_search(tg.problem0)
print("Sequence to find solution: ", solution(dfs.NODE_LIST))
print("Number of expanded nodes to find solution: ", dfs.NUM_EXPANDED)
#bfs.breadth_first_search(tg.problem0)
#print("Sequence to find solution: ", solution(bfs.NODE_LIST))
#print("Number of expanded nodes to find solution: ", bfs.NUM_EXPANDED)

print("\nProblem 2")
bfs.breadth_first_search(tg.problem1)
print("Sequence to find solution: ", solution(bfs.NODE_LIST))
print("Number of expanded nodes to find solution: ", bfs.NUM_EXPANDED)

    print("\nProblem 3")
bfs.breadth_first_search(tg.problem2)
print("Sequence to find solution: ", solution(bfs.NODE_LIST))
print("Number of expanded nodes to find solution: ", bfs.NUM_EXPANDED)

print("\nProblem 4")
bfs.breadth_first_search(tg.problem3)
print("Sequence to find solution: ", solution(bfs.NODE_LIST))
print("Number of expanded nodes to find solution: ", bfs.NUM_EXPANDED)

print("\nProblem 5")
bfs.breadth_first_search(tg.problem4)
print("Sequence to find solution: ", solution(bfs.NODE_LIST))
print("Number of expanded nodes to find solution: ", bfs.NUM_EXPANDED)

print("\nProblem 6")
bfs.breadth_first_search(tg.problem5)
print("Sequence to find solution: ", solution(bfs.NODE_LIST))
print("Number of expanded nodes to find solution: ", bfs.NUM_EXPANDED)

print("\nProblem 7")
bfs.breadth_first_search(tg.problem6)
print("Sequence to find solution: ", solution(bfs.NODE_LIST))
print("Number of expanded nodes to find solution: ", bfs.NUM_EXPANDED)

print("\nProblem 8")
bfs.breadth_first_search(tg.problem7)
print("Sequence to find solution: ", solution(bfs.NODE_LIST))
print("Number of expanded nodes to find solution: ", bfs.NUM_EXPANDED)

print("\nProblem 9")
bfs.breadth_first_search(tg.problem8)
print("Sequence to find solution: ", solution(bfs.NODE_LIST))
print("Number of expanded nodes to find solution: ", bfs.NUM_EXPANDED)

print("\nProblem 10")
bfs.breadth_first_search(tg.problem9)
print("Sequence to find solution: ", solution(bfs.NODE_LIST))
print("Number of expanded nodes to find solution: ", bfs.NUM_EXPANDED)
        
print("Problem 11")
bfs.breadth_first_search(tg.problem10)
print("Sequence to find solution: ", solution(bfs.NODE_LIST))
print("Number of expanded nodes to find solution: ", bfs.NUM_EXPANDED)

print("\nProblem 12")
bfs.breadth_first_search(tg.problem11)
print("Sequence to find solution: ", solution(bfs.NODE_LIST))
print("Number of expanded nodes to find solution: ", bfs.NUM_EXPANDED)

print("\nProblem 13")
bfs.breadth_first_search(tg.problem12)
print("Sequence to find solution: ", solution(bfs.NODE_LIST))
print("Number of expanded nodes to find solution: ", bfs.NUM_EXPANDED)

print("\nProblem 14")
bfs.breadth_first_search(tg.problem13)
print("Sequence to find solution: ", solution(bfs.NODE_LIST))
print("Number of expanded nodes to find solution: ", bfs.NUM_EXPANDED)

print("\nProblem 15")
bfs.breadth_first_search(tg.problem14)
print("Sequence to find solution: ", solution(bfs.NODE_LIST))
print("Number of expanded nodes to find solution: ", bfs.NUM_EXPANDED)

print("\nProblem 16")
bfs.breadth_first_search(tg.problem15)
print("Sequence to find solution: ", solution(bfs.NODE_LIST))
print("Number of expanded nodes to find solution: ", bfs.NUM_EXPANDED)

print("\nProblem 17")
bfs.breadth_first_search(tg.problem16)
print("Sequence to find solution: ", solution(bfs.NODE_LIST))
print("Number of expanded nodes to find solution: ", bfs.NUM_EXPANDED)

print("\nProblem 18")
bfs.breadth_first_search(tg.problem17)
print("Sequence to find solution: ", solution(bfs.NODE_LIST))
print("Number of expanded nodes to find solution: ", bfs.NUM_EXPANDED)

print("\nProblem 19")
bfs.breadth_first_search(tg.problem18)
print("Sequence to find solution: ", solution(bfs.NODE_LIST))
print("Number of expanded nodes to find solution: ", bfs.NUM_EXPANDED)

print("\nProblem 20")
bfs.breadth_first_search(tg.problem19)
print("Sequence to find solution: ", solution(bfs.NODE_LIST))
print("Number of expanded nodes to find solution: ", bfs.NUM_EXPANDED)

tg.StateDimension = 4

print("Problem 21")
bfs.breadth_first_search(tg.problem20)
print("Sequence to find solution: ", solution(bfs.NODE_LIST))
print("Number of expanded nodes to find solution: ", bfs.NUM_EXPANDED)

print("\nProblem 22")
bfs.breadth_first_search(tg.problem21)
print("Sequence to find solution: ", solution(bfs.NODE_LIST))
print("Number of expanded nodes to find solution: ", bfs.NUM_EXPANDED)

print("\nProblem 23")
bfs.breadth_first_search(tg.problem22)
print("Sequence to find solution: ", solution(bfs.NODE_LIST))
print("Number of expanded nodes to find solution: ", bfs.NUM_EXPANDED)

print("\nProblem 24")
bfs.breadth_first_search(tg.problem23)
print("Sequence to find solution: ", solution(bfs.NODE_LIST))
print("Number of expanded nodes to find solution: ", bfs.NUM_EXPANDED)

print("\nProblem 25")
bfs.breadth_first_search(tg.problem24)
print("Sequence to find solution: ", solution(bfs.NODE_LIST))
print("Number of expanded nodes to find solution: ", bfs.NUM_EXPANDED)

Difficult

print("\nProblem 26")
bfs.breadth_first_search(tg.problem25)
print("Sequence to find solution: ", solution(bfs.NODE_LIST))
print("Number of expanded nodes to find solution: ", bfs.NUM_EXPANDED)

print("\nProblem 27")
bfs.breadth_first_search(tg.problem26)
print("Sequence to find solution: ", solution(bfs.NODE_LIST))
print("Number of expanded nodes to find solution: ", bfs.NUM_EXPANDED)

print("\nProblem 28")
bfs.breadth_first_search(tg.problem27)
print("Sequence to find solution: ", solution(bfs.NODE_LIST))
print("Number of expanded nodes to find solution: ", bfs.NUM_EXPANDED)

print("\nProblem 29")
bfs.breadth_first_search(tg.problem28)
print("Sequence to find solution: ", solution(bfs.NODE_LIST))
print("Number of expanded nodes to find solution: ", bfs.NUM_EXPANDED)

print("\nProblem 30")
bfs.breadth_first_search(tg.problem29)
print("Sequence to find solution: ", solution(bfs.NODE_LIST))
print("Number of expanded nodes to find solution: ", bfs.NUM_EXPANDED)
"""
