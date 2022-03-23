'''
Find the goal from the Start Node using uninformed strategies (Depth First and
Breadt First) and see what happens. Then proceed to an informed strategy
(Hill climbing). 
a) A Depth First Search
b) A breadth First Search
c) Hill climbing
'''


from collections import defaultdict


# use Python structure dictionary to create the adjacency list.
# The numbers in dictionary are heuristic distance from that node to goal node.
# The heuristic distance is estimated.
adjacencyList = {'S': [('A', 10.4), ('D', 8.9)],
                 'A': [('S', 11), ('B',6.7), ('D', 8.9)],
                 'B': [('A', 10.4), ('C', 4), ('E', 6.9)],
                 'C': [('B', 6.7)],
                 'D': [('S', 11), ('A', 10.4),('E', 6.9)],
                 'E': [('D', 8.9), ('B', 6.7), ('F', 3)],
                 'F': [('E', 6.9), ('G', 0)],
                 'G': [('F', 3)]}





# create a function to perform depth first search
def depth_first_search(start,goal):
    stack = []
    stack.append(start)   #put the start node into the stack.
    visitedList[start] = True 
    
    while stack:   #wihle loop. while the stack is not empty.
        poppednode = stack.pop()    #remove the last node in the stack (LIFO).
        print(poppednode, end = " ")   #print the popped node in a line.
           
        if poppednode == goal:   #check if we reach to the goal
            print ('\nReached goal.')
            return 
        else:
            #use for loop to traverse the nodes in depth first manner:
            for neighbor in adjacencyList[poppednode]:
                if visitedList[neighbor[0]] == False:   #If we didn't visited the node before
                    stack.append(neighbor[0])     #add the unvisited node into the stack
                    visitedList[neighbor[0]] = True #mark the node as visited

visitedList = defaultdict(int)  #Before we start DFS,set all the nodes as not visited.
print ('The sequence of DFS is: ')
depth_first_search("S","G")



# create a function to perform breadth first search:
def breadth_first_search(start,goal):
    queue = []    #initial an empty queue.
    queue.append(start)    #put the start node into the queue
    visitedList[start] = True  #mark the start node as visited
    
    while queue:  #while loop. while queue in not empty.
        poppednode = queue.pop(0)    #remove the first elements in the queue (FIFO)
        print(poppednode, end = " ")
           
        if poppednode == goal:    #check if we reach to the goal
            print ('\nReached goal.')
            return 
        else:
            #use for loop to traverse the node in bread first manner:
            for neighbor in adjacencyList[poppednode]:
                if visitedList[neighbor[0]] == False: #If the node neighbor is not visited before
                    queue.append(neighbor[0]) #add the node neighbor into queue
                    visitedList[neighbor[0]] = True 

visitedList = defaultdict(int) #set all the nodes as not visited before BFS start.
print ('\nThe sequence of BFS is: ')
breadth_first_search("S","G")



# create a function to perform Hill Climbing Search:
def hill_climb(start,goal):
    queue = []   #initial an empty queue
    queue.append(start)  #add the start node into the queue
    visitedList[start] = True  #mark start node as visited
    lowestcost = float("inf")  #initial the lowest cost as infinit 
    min_node = None #initial the node with the lowest cost
    
    while queue:  #while loop. while queue is not empty
        poppednode = queue.pop(0)   #remove the first node from queue
        print(poppednode, end = " ")
            
        if poppednode == goal:   #check if we reach to the goal
            print ('\nReached goal.')
            return 
        else:
            #use for loop to traverse the node in hill climbing manner:
            for neighbor,distance in adjacencyList[poppednode]:
                # if the neighbor node of popped node was not visited,
                # and the cost of neighbor node is less:
                if visitedList[neighbor] == False and lowestcost > distance:
                    visitedList[neighbor] = True  
                    lowestcost = distance #give the estimated heuristic distance to the variable lowestcost
                    min_node = neighbor #min_node become one of the children/neighbor node with least cost so far.
            queue.append(min_node) # add the children node with least cost into queue.

visitedList = defaultdict(int) #initially set all the nodes as unvisited in the beginning of Hill Climbing.
print ('\nThe sequence of Hill Climbing is: ')
hill_climb("S","G")


