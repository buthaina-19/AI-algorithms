# BY. BUTHAINA SAMI
# Import needed predefined Libraries #
import networkx as nx
import matplotlib.pylab as plt
import queue

#------------------------------------------------------------------------------------------------------------
# Represent Romaina map as Graph #
g = nx.Graph()
g.add_edge('Arad', 'Sibiu', weghit= 140)
g.add_edge('Arad', 'Timisoara', weghit=118 )
g.add_edge('Arad', 'Zerind', weghit=75 )
g.add_edge('Bucharest', 'Fagaras', weghit=211 )
g.add_edge('Bucharest', 'Giurgiu', weghit=90 )
g.add_edge('Bucharest', 'Pitesti', weghit=101 )
g.add_edge('Bucharest', 'Urziceni', weghit=85 )
g.add_edge('Craiova', 'Dobreta', weghit=120 )
g.add_edge('Craiova', 'Pitesti', weghit=138 )
g.add_edge('Craiova', 'Rimnicu_Vilcea', weghit=146 )
g.add_edge('Dobreta', 'Mehadia', weghit=75 )
g.add_edge('Eforie', 'Hirsova', weghit=86)
g.add_edge('Fagaras', 'Sibiu', weghit=99 )
g.add_edge('Hirsova', 'Urziceni', weghit=98 )
g.add_edge('Iasi', 'Neamt', weghit=87 )
g.add_edge('Iasi', 'Vaslui', weghit=92 )
g.add_edge('Lugoj', 'Mehadia', weghit=70 )
g.add_edge('Lugoj', 'Timisoara', weghit=111 )
g.add_edge('Oradea', 'Zerind', weghit=71 )
g.add_edge('Oradea', 'Sibiu', weghit=151 )
g.add_edge('Pitesti', 'Rimnicu_Vilcea', weghit=97 )
g.add_edge('Rimnicu_Vilcea', 'Sibiu', weghit=80 )
g.add_edge('Urziceni', 'Vaslui', weghit=142 )

#nx.draw_spring(g, with_labels=True, node_color='yellow',font_size=12)
#plt.show()

#------------------------------------------------------------------------------------------------------------
# Breadth First Search Algorithm #
def bfs(g,initial):
    Goal='Bucharest'  #specify Goal city in our case. 
    visited=set()     #create an empty visited set so no city can be duplicate.
    q= queue.Queue()  #create a queue to store opened cities.
    q.put(initial)    #add first city to the queue.
    order=[]          #create an empty list to store Path in a correct way.

    while not q.empty(): #while queue not empty.
        current =q.get() #store last added city as current. 
        
        if current not in visited :    #if current city not visited yet.
            order.append(current)      #add current city to path. 
            visited.add(current)       #mark current city as visited. 
            if Goal is current:        #if current city is our GOAL. 
               return order            #retrieve PATH.
            else:                      #current city is not our GOAL.
             for city in g[current]:   #for each city next to current city.  
                if city not in visited:#check whether that city has been visited.
                    q.put(city)        #add city to open cities Queue.
    return None

#------------------------------------------------------------------------------------------------------------
### MAIN PROGRAM ###
starting_city= input('\nWhat is your starting City? (1st letter in CAPITAL)\n') #Askin user for starting city.
find_path = bfs(g,starting_city)                                   #Bredth First Search Algorithm Function CALL.
if find_path: 
   print('\nPath found! \n\n form {} to {}: \n {}\n'.format(starting_city,'Bucharest',find_path))
else:
  print('could NOT find a path !!')