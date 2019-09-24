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
        queue = [] 
  
        
        queue.append(s) 
        visited[s] = True
  
        while queue: 
            s = queue.pop(0) 
            print(s) 
            for i in self.graph[s]: 
                
                if visited[i] == False: 
                    queue.append(i) 
                    visited[i] = True
    
    def DFSUtil(self, v, visited): 
        # Mark the current node as visited  
        # and print it 
        visited[v] = True
        print(v) 
  
        # Recur for all the vertices  
        # adjacent to this vertex 
        for i in self.graph[v]:
            print(str(v)+ "n") 
            if visited[i] == False: 
                print(str(i)+"H")
                self.DFSUtil(i, visited) 
  
    # The function to do DFS traversal. It uses 
    # recursive DFSUtil() 

    def DFS(self, v): 
  
        # Mark all the vertices as not visited 
        visited = [False] * (len(self.graph)) 
  
        # Call the recursive helper function  
        # to print DFS traversal 
        self.DFSUtil(v, visited) 


graph = Graph()

graph.addEdge(0, 1) 
graph.addEdge(0, 2) 
graph.addEdge(2, 3) 
graph.addEdge(2, 4) 
graph.addEdge(4, 5) 
graph.addEdge(4, 6) 
graph.addEdge(4, 7)
graph.addEdge(3, 7) 
graph.addEdge(3, 8) 
graph.addEdge(6, 8) 

#graph.BFS(0)
graph.DFS(0)