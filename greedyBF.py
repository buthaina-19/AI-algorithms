# by. BUTHAINA SAMI
# representing romaina map & heuristic function AS dictionary #
romainGraph = {
    'Arad': ['Sibiu', 'Zerind', 'Timisoara'],
    'Zerind': ['Arad', 'Oradea'],
    'Oradea': ['Zerind', 'Sibiu'],
    'Sibiu': ['Arad', 'Oradea', 'Fagaras', 'Rimnicu'],
    'Timisoara': ['Arad', 'Lugoj'],
    'Lugoj': ['Timisoara', 'Mehadia'],
    'Mehadia': ['Lugoj', 'Drobeta'],
    'Drobeta': ['Mehadia', 'Craiova'],
    'Craiova': ['Drobeta', 'Rimnicu', 'Pitesti'],
    'Rimnicu': ['Sibiu', 'Craiova', 'Pitesti'],
    'Fagaras': ['Sibiu', 'Bucharest'],
    'Pitesti': ['Rimnicu', 'Craiova', 'Bucharest'],
    'Bucharest': ['Fagaras', 'Pitesti', 'Giurgiu', 'Urziceni'],
    'Giurgiu': ['Bucharest'],
    'Urziceni': ['Bucharest', 'Vaslui', 'Hirsova'],
    'Hirsova': ['Urziceni', 'Eforie'],
    'Eforie': ['Hirsova'],
    'Vaslui': ['Iasi', 'Urziceni'],
    'Iasi': ['Vaslui', 'Neamt'],
    'Neamt': ['Iasi']
}
heuristic = {
    'Arad' : [366],
    'Bucharest':[0],
    'Craiova':[160],
    'Drobeta' :[242],
    'Eforie': [161],
    'Fagaras': [178],
    'Giurgiu': [77],
    'Hirsova':[151],
    'Iasi': [226],
    'Lugoj':[244],
    'Mehadia': [241],
    'Neamt':[234],
    'Oradea':[380],
    'Pitesti': [98],
    'Rimnicu': [193],
    'Sibiu':[253],
    'Timisoara': [329],
    'Urziceni': [80],
    'Vaslui': [199],
    'Zerind': [374]
}

#------------------------------------------------------------------------------------------------------------
# Greedy best first search Algorithm # 
def gbf(graph, heuristic, initial):
    goal='Bucharest'                                    #initialize our Goal 
    visited = []                                        #creat empty list to store cities from intital to goal city.
    priority_queue = [(heuristic[initial][0], initial)] #Store initial city with its heuristic value in frontier list.
    
    while priority_queue:                   #while frontier list not empty.
        priority_queue.sort(reverse=True)   #sort the queue based on heuristic value in descending order.
        current = priority_queue.pop()[1]   #store the lowest value from frontier as current node.
        visited.append(current)             #ADD lowest heuistic city value to visited (closed) list. 
        
        if current == goal:    #if node we are plan to expand was our GOAL.
            return visited     #stop and return the path (visited)list.
        
        childs = graph[current]                                   #if not store its childerens(neighbors). 
        for city in childs:                                       #for each city in current node(city) childrens. 
            if city not in visited:                               #check if we already visit that city. 
                priority_queue.append((heuristic[city][0], city)) #if not ADD each to frontier list with its hueristic value.
    
    return None

#------------------------------------------------------------------------------------------------------------
### MAIN PROGRAM ###
starting_city= input('\nWhat is your starting City? (1st letter in CAPITAL)\n') #Askin user for starting city.
find_path =gbf(romainGraph,heuristic,starting_city)                                   #Bredth First Search Algorithm Function CALL.
if find_path: 
   print('\nPath found! \n\n form {} to {}: \n {}\n'.format(starting_city,'Bucharest',find_path))
else:
  print('could NOT find a path !!')
