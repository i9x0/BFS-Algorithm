

Map = {
    'Sakaka': ['Zloum', 'gara'],
    'Zloum': ['Arar', 'Swier'],
    'gara': ['Domah'],
    'ARAR': [],
    'Swier': ['Sakaka'],
    'Domah': []
}



def bfs(Map, start, Goal):
    #Queue start in user do want
    queue = [[start]]
    #visited take unice value  
    visited = set()
    #start looping *in pyhton boolean is while queue have value a queue is true we can repalce queue to true but some Scenario return Error *
    while queue:
    #path now  value set by the user, which represents the starting point
        path = queue.pop(0)
        
        
        #here take last value in path
        vertex = path[-1]
        #check vertex is goal --if tue end return path and end program
        if vertex == Goal:
            return path
        # We check if the current node is already in the visited nodes set in order not to recheck it
        elif vertex not in visited:
            # enumerate all adjacent nodes, construct a new path and push it into the queue
                #current_neighbour take all cities in vertex
            for current_neighbour in Map.get(vertex,[]):
                #new path take a copy path 
                #[:] is mean take copy from path 
                new_path = path[:]
                
                new_path.append(current_neighbour)
               
                queue.append(new_path)
            visited.add(vertex)

            
print(bfs(Map, 'Sakaka', "Swier"))
