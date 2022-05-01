import tilegame as tg
import breadthfirstsearch as bfs
import depthfirstsearch as dfs
import iterativedeepeningdfs as idfs
import astarsearch as astar
import iterativedeepeningastar as iastar
import time as t
import idas as ida

def result(state, action):
    i = state.index('0')
    newState = list(state)
    row,col=i//tg.StateDimension, i % tg.StateDimension
    
    if ((action=='u' and row==0) or
        (action=='d' and row==tg.StateDimension-1) or
        (action=='l' and col==0) or
        (action=='r' and col==tg.StateDimension-1)):
        return newState
    if action=='u':
        l,r = row*tg.StateDimension+col, (row-1)*tg.StateDimension+col
    elif action=='d':
        l,r = row*tg.StateDimension+col, (row+1)*tg.StateDimension+col
    elif action=='l':
        l,r = row*tg.StateDimension+col, row*tg.StateDimension+col-1
    elif action=='r' :
        l,r = row*tg.StateDimension+col, row*tg.StateDimension+col+1
    newState[l], newState[r] = newState[r], newState[l] 
    return ''.join(newState)

"""
function calls class Node method to get the sequence for the solution of the puzzle.
each algorithm contains its own Node class
"""
def solution(nodes):
    return nodes.node_list()

"""
Uses List with actions, "root" is first element,
to test solutions produced from algorithms
"""
def test_results(movesList,ind):
    states = []
    newState = tg.problems[ind].initial
    
    for i in range(len(movesList)):
        if(movesList[i] == "root"):
            states.append(tg.problems[ind].initial)
        else:
            states.append(result(newState,movesList[i]))
            newState = result(newState,movesList[i])
        
    return states
    

"""
Each for loop executes an algorithm on all the problems.

"""
#bfs with one million expanded nodes limit
for i in range(30):
    
    if i >= 20:
        tg.StateDimension = 4
    else:
        tg.StateDimension = 3
        
    print("PROBLEM: ", i)
    tic = t.perf_counter()
    results = bfs.breadth_first_search(tg.problems[i])
    toc = t.perf_counter()
    
    if(results == False):
        print("Expanded node limit reached")
        print("Number of expanded nodes: ", bfs.NUM_EXPANDED, "\n")
        print(f"Time to find solution: {toc-tic:0.4f} seconds")
        print()
    else:
        if(results != "BFS failed!"):
            results_list = solution(results)
            print("Sequence: ", results_list)
            print("Testing results: ", test_results(results_list,i))
            
        print("Number of expanded nodes: ", bfs.NUM_EXPANDED, "\n")
        print(f"Time to find solution: {toc-tic:0.4f} seconds")
        print()
"""
#dfs one million expanded nodes cap
for i in range(30):
    
    if i >= 20:
        tg.StateDimension = 4
    else:
        tg.StateDimension = 3
        
    print("PROBLEM: ", i)
    tic = t.perf_counter()
    results = dfs.depth_first_search(tg.problems[i])
    toc = t.perf_counter()
    
    if(results == False):
        print("Expanded node limit reached")
        print("Number of expanded nodes: ", dfs.NUM_EXPANDED, "\n")
        print(f"Time to find solution: {toc-tic:0.4f} seconds")
        print()
    else:
        if(results != "DFS failed!"):
            results_list = solution(results)
            print("Sequence: ", results_list)
            print("Testing results: ", test_results(results_list,i))
            
        print("Number of expanded nodes: ", dfs.NUM_EXPANDED, "\n")
        print(f"Time to find solution: {toc-tic:0.4f} seconds")
        print()
"""
"""
#iddfs one million expanded nodes cap
for i in range(30):
    
    if i >= 20:
        tg.StateDimension = 4
    else:
        tg.StateDimension = 3
        
    print("PROBLEM: ", i)
    tic = t.perf_counter()
    results = idfs.iterative_deepening_search(tg.problems[i])
    toc = t.perf_counter()
    
    if(results == False):
        print("Expanded node limit reached")
        print("Number of expanded nodes: ", idfs.STORE_NUM_EXPANDED, "\n")
        print(f"Time to find solution: {toc-tic:0.4f} seconds")
        print()
    else:
        if(results != "IDDFS failed!"):
            results_list = solution(results)
            print("Sequence: ", results_list)
            print("Testing results: ", test_results(results_list,i))
            
        print("Number of expanded nodes: ", idfs.STORE_NUM_EXPANDED, "\n")
        print(f"Time to find solution: {toc-tic:0.4f} seconds")
        print()
"""
"""
#A* one hundred thousand expanded node cap
for i in range(30):
    
    if i >= 20:
        tg.StateDimension = 4
    else:
        tg.StateDimension = 3
        
    print("PROBLEM: ", i)
    tic = t.perf_counter()
    results = astar.a_star_search(tg.problems[i])
    toc = t.perf_counter()
    
    if(results == False):
        print("Expanded node limit reached")
        print("Number of expanded nodes: ", astar.NUM_EXPANDED, "\n")
        print(f"Time to find solution: {toc-tic:0.4f} seconds")
        print()
    else:
        if(results != "A* failed!"):
            results_list = solution(results)
            print("Sequence: ", results_list)
            print("Testing results: ", test_results(results_list,i))
            
        print("Number of expanded nodes: ", astar.NUM_EXPANDED, "\n")
        print(f"Time to find solution: {toc-tic:0.4f} seconds")
        print()
"""
"""
#IDA* one hundred thousand expanded node cap
for i in range(30):
    
    if i >= 20:
        tg.StateDimension = 4
    else:
        tg.StateDimension = 3
        
    print("PROBLEM: ", i)
    tic = t.perf_counter()
    results = iastar.iterative_deepening_a_star_search(tg.problems[i])
    toc = t.perf_counter()
    
    if(results == False):
        print("Expanded node limit reached")
        print("Number of expanded nodes: ", iastar.NUM_EXPANDED, "\n")
        print(f"Time to find solution: {toc-tic:0.4f} seconds")
        print()
    else:
        results_list = solution(results)
        print("Sequence: ", results_list)
        print("Testing results: ", test_results(results_list,i))
        print("Number of expanded nodes: ", iastar.NUM_EXPANDED, "\n")
        print(f"Time to find solution: {toc-tic:0.4f} seconds")
        print()
"""
