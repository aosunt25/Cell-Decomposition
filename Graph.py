from collections import defaultdict

class Graph():
    # Constructor
    # 
#    lista = ["D","A","B","C","G","E"] 
    def __init__(self): 
        self.graph = defaultdict(list)  
        

    def addEdge(self,u,v): 
        self.graph[u].append(v) 
  
     
    def BFS(self, s): 
  
        visited = [False] * (len(self.graph)) 
        print("visited len: ", len(visited)+1)
        print("graph len: ", len(self.graph))
        queue = [] 
  
        
        queue.append(s) 
        visited[s] = True
        print("BFS")
        
        while queue: 
            
            s = queue.pop(0)
            
            print(s)
            #print(end = " ") 
            #print("-",self.graph[s]) 
            for i in self.graph[s]:                
                if visited[i] == False:   
                    queue.append(i) 
                    #print(queue)
                    visited[i] = True
    

    def DFSUtil(self, v, visited): 
        # Mark the current node as visited  
        # and print it 
        visited[v] = True
        print(v) 
  
        # Recur for all the vertices  
        # adjacent to this vertex 
        for i in self.graph[v]:
            if visited[i] == False: 
                self.DFSUtil(i, visited) 
  
    # The function to do DFS traversal. It uses 
    # recursive DFSUtil() 

    def DFS(self, v): 
        print("DFS")
        # Mark all the vertices as not visited 
        visited = [False] * (len(self.graph)) 
  
        # Call the recursive helper function  
        # to print DFS traversal 
        self.DFSUtil(v, visited) 

