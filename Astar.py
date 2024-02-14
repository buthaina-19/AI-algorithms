# A* algorithm BY. BUTHAINA SAMI
#Importing needed library to store values 
import heapq

#------------------------------------------------------------------------------------------------------------
#Represent Romania map with edges weight & heuristic function as Dictionaries
romainGraph = {
    'Arad': [('Sibiu',140), ('Zerind',75), ('Timisoara',118)],
    'Zerind': ['Arad', 'Oradea'],
    'Oradea': [('Zerind',71), ('Sibiu',151)],
    'Sibiu': [('Arad',140), ('Oradea',151), ('Fagaras',99), ('Rimnicu',80)],
    'Timisoara': [('Arad',118), ('Lugoj',111)],
    'Lugoj': [('Timisoara',111), ('Mehadia',70)],
    'Mehadia': [('Lugoj',70), ('Dobreta',75)],
    'Dobreta': [('Mehadia',75), ('Craiova',120)],
    'Craiova': [('Dobreta',120), ('Rimnicu',146), ('Pitesti',138)],
    'Rimnicu': [('Sibiu',80), ('Craiova',146), ('Pitesti',97)],
    'Fagaras': [('Sibiu',99), ('Bucharest',211)],
    'Pitesti': [('Rimnicu',97), ('Craiova',138), ('Bucharest',101)],
    'Bucharest': [('Fagaras',211), ('Pitesti',101), ('Giurgiu',90), ('Urziceni',85)],
    'Giurgiu': [('Bucharest',90)],
    'Urziceni': [('Bucharest',85), ('Vaslui',142), ('Hirsova',98)],
    'Hirsova': [('Urziceni',98), ('Eforie',86)],
    'Eforie': [('Hirsova',86)],
    'Vaslui': [('Iasi',92), ('Urziceni',142)],
    'Iasi': [('Vaslui',92), ('Neamt',87)],
    'Neamt': [('Iasi',87)]
}

heuristic = {
    'Arad' : 366,
    'Bucharest':0,
    'Craiova':160,
    'Dobreta' :242,
    'Eforie': 161,
    'Fagaras': 178,
    'Giurgiu': 77,
    'Hirsova':151,
    'Iasi': 226,
    'Lugoj':244,
    'Mehadia': 241,
    'Neamt':234,
    'Oradea':380,
    'Pitesti': 98,
    'Rimnicu': 193,
    'Sibiu':253,
    'Timisoara': 329,
    'Urziceni': 80,
    'Vaslui': 199,
    'Zerind': 374
}

#------------------------------------------------------------------------------------------------------------
# A-star search Algorithm function #
def A_star(graph, heuristic, start): 
    goal='Bucharest'          #initialize our Goal 
    visited = set()           #create empty set to keep track visited cities(opened)
    priority_queue = []       #create empty list to choose the lowest value 

    #we will push the starting city with its heuristic value & distance from begining witch is 0 
    #as tubule to priority_queue 
    heapq.heappush(priority_queue, (heuristic[start], 0, start, [start]))

    while priority_queue:  #while priority queue not empty 

        #assign lowest value in heap to path, current node, cost 
        _, cost, current, path = heapq.heappop(priority_queue)


        if current == goal:     #If current nod is Our Goal 
            return path         #then return path 
        
        if current not in visited:         #check if we already visit that city. 
            visited.add(current)           #If Not then add that city to visited set>
            childerns = graph[current]     #store its childerens(neighbors) cities. 
            
            for city, city_cost in  childerns:         #for each city for current node(city)childrens.
                cost_so_far = cost + city_cost         #calculate|update COST SO FAR g(n)
                total = cost_so_far + heuristic[city]  #calculate total cost f(n) = g(n)+h(n)
                new_path = path + [city]               #store|add the new city to old path 
                
                #push|add that city to priority queue with it information(total cost, cost so far, city, its path)
                heapq.heappush(priority_queue, (total, cost_so_far, city, new_path))
    
    return None

#------------------------------------------------------------------------------------------------------------
### MAIN PROGRAM ###
starting_city= input('\nWhat is your starting City? (1st letter in CAPITAL)\n')                   #Asking user for starting city.
find_path =A_star(romainGraph,heuristic,starting_city)                                            #A-Star Search Algorithm Function CALL.
if find_path:                                                                                     #if find_path can return a path.
   print('\nPath found! \n\n form {} to {}: \n {}\n'.format(starting_city,'Bucharest',find_path)) #print that path. 
else:                                                                                             #if not return this error msg.
  print('could NOT find a path !!')