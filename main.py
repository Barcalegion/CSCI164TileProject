import tilegame as tg
import breadthfirstsearch as bfs
import depthfirstsearch as dfs
import iterativedeepeningdfs as idfs
import astarsearch as astar
import iterativedeepeningastar as iastar
import time as t

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


tic = t.perf_counter()
astar.a_star_search(tg.problems[30])
toc = t.perf_counter()
print("Sequence to find solution: ", solution(astar.NODE_LIST))
print("Number of expanded nodes to find solution: ", astar.NUM_EXPANDED)
print(f"Time taken to find solution: {toc-tic:0.4f} seconds")

tic = t.perf_counter()
astar.a_star_search(tg.problems[31])
toc = t.perf_counter()
print("Sequence to find solution: ", solution(astar.NODE_LIST))
print("Number of expanded nodes to find solution: ", astar.NUM_EXPANDED)
print(f"Time taken to find solution: {toc-tic:0.4f} seconds")

tic = t.perf_counter()
astar.a_star_search(tg.problems[32])
toc = t.perf_counter()
print("Sequence to find solution: ", solution(astar.NODE_LIST))
print("Number of expanded nodes to find solution: ", astar.NUM_EXPANDED)
print(f"Time taken to find solution: {toc-tic:0.4f} seconds")

tic = t.perf_counter()
astar.a_star_search(tg.problems[33])
toc = t.perf_counter()
print("Sequence to find solution: ", solution(astar.NODE_LIST))
print("Number of expanded nodes to find solution: ", astar.NUM_EXPANDED)
print(f"Time taken to find solution: {toc-tic:0.4f} seconds")

"""
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
    dfs.depth_first_search(tg.problems[i])
    print("Sequence to find solution: ", solution(dfs.NODE_LIST))
    print("Number of expanded nodes to find solution: ", dfs.NUM_EXPANDED, "\n")
"""
"""
#iterative deepening depth first search
for i in range(30):
    if i == 20:
        tg.StateDimension = 4
    print("PROBLEM: ", i)
    idfs.iterative_deepening_search(tg.problems[i])
    print("Sequence to find solution: ", solution(idfs.NODE_LIST))
    print("Number of expanded nodes to find solution: ", idfs.NUM_EXPANDED, "\n")
"""
"""
#a star search
for i in range(30):
    if i == 20:
        tg.StateDimension = 4
    print("PROBLEM: ", i)
    astar.a_star_search(tg.problems[i])
    print("Sequence to find solution: ", solution(astar.NODE_LIST))
    print("Number of expanded nodes to find solution: ", astar.NUM_EXPANDED, "\n")
"""
"""
#iterative deepening a star
for i in range(30):
    if i == 20:
        tg.StateDimension = 4
    print("PROBLEM: ", i)
    iastar.iterative_deepening_a_star_search(tg.problems[i])
    #print("Sequence to find solution: ", solution(astar.NODE_LIST))
    #print("Number of expanded nodes to find solution: ", astar.NUM_EXPANDED, "\n")
"""
