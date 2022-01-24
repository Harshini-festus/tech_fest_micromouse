# import numpy as np
from collections import deque

class dfs:
    def __init__(self,map,M,N,x_i,y_i,x_f,y_f):
        self.map=map
        self.M=M
        self.N=N
        self.visited=visited = [[False for x in range(self.N)] for y in range(self.M)]
        self.cost=[[0 for x in range(self.N)] for y in range(self.M)]
        self.q=deque()
        self.dist=0
        self.free_neigh=deque()
        self.x_i=x_i
        self.y_i=y_i
        self.x_f=x_f
        self.y_f=y_f
        self.route=[]
        self.min_dist=float('inf')
        self.row=[1,0,0,-1] #left and right
        self.col=[0,1,-1,0] #top and bottom
        self.a=[[100 for x in range(self.N)] for y in range(self.M)]
        
    
    def matrix_update(self,i,j):
        if (i,j,self.dist+1) not in self.q:
            self.q.append((i,j,self.dist+1))
            # print(self.q)
        self.visited[i][j]=True
        # print(self.visited)
        self.cost[i][j]=self.dist + 1
        print(self.cost)
    
    def free_node(self,i,j): #this will give me the priority of node to choose
        # 0 means free space
        
        min=0
        for k in range(4):
            print("--------")
            print(k)
            i_neigh=i+self.row[k]
            j_neigh=j+self.col[k]
            if i_neigh < 0 or j_neigh < 0 or i_neigh > self.M-1 or j_neigh > self.N-1:
                return
            if self.visited[i_neigh][j_neigh]:
                return
            # checking for free space 
            if self.map[i_neigh][j_neigh]==0:    
                self.a[i_neigh][j_neigh]=abs((i_neigh+j_neigh)-(self.x_f+self.y_f))
                # print(a[i][j])
            
            min=self.a[i_neigh][j_neigh]
        for l in range(4):
            i_neigh=i+self.row[k]
            j_neigh=j+self.col[k]
            if i_neigh < 0 or j_neigh < 0 or i_neigh > self.M-1 or j_neigh > self.N-1:
                return
            if self.visited[i_neigh][j_neigh]:
                return
            if self.a[i_neigh][j_neigh]<=min:
                min=self.a[i_neigh][j_neigh]
                print(min)
                # print("------")
                if (i_neigh,j_neigh) not in self.free_neigh:
                    self.free_neigh.append((i,j)) #last added one has more importance than the before one so use only pop
                # print(self.free_neigh)               
        print(self.free_neigh)
        
        # return int(i_next), int(j_next)
            
    def traversal(self):
        #i and j are the current nodes I am standing in
        i=self.x_i
        j=self.y_i
        i_next=0
        j_next=0
        if i == self.x_f and j == self.y_f:
            # self.min_dist = self.dist
            print("--------goal reached---------")
            print(self.route)
            return 
        while (i,j)!= (self.x_f,self.y_f):    
            self.free_node(i, j)
            i_prev=0
            j_prev=0
            # print(self.free_neigh)
            while self.free_neigh:
                (i,j)=self.free_neigh.pop()
                self.matrix_update(i, j)
                self.route.append((i,j))
                i_prev=i
                j_prev=j
                
            if len(self.free_neigh)==0:
                print("destination can't be reached from the given route")
                self.route.pop()
                self.free_node(i_prev, j_prev)
        if self.min_dist == float('inf'):
            print("Destination can't be reached from given source")
            return -1
        
        # return final_value
    
    # def path(self):
    #     if self.min_dist == float('inf'):
    #         print("Destination can't be reached from given source")
    #         return -1
        
    #     print("The shortest path from source to destination has length", self.min_dist)
    #     while self.dist!=1:
    #       for k in range(4):
    #         if self.cost[i + self.row[k]][j + self.col[k]] == dist-1:
    #             i, j, dist = i + self.row[k], j + self.col[k], dist-1
    #             self.route.append((i,j))
    #             break
    #     self.route.append((self.x_i, self.y_i))
    #     self.route = self.route[::-1]
    #     # Finding list of turns
    #     turns = []
    #     # I want prev point and next point to be sharing a corner, meaning I took a turn
    #     for i in range(1,len(self.route)-1):
    #         prev_pt = self.route[i-1]
    #         curr_pt = self.route[i]
    #         next_pt = self.route[i+1]
    #     if prev_pt[0]!=next_pt[0] and prev_pt[1]!=next_pt[1]:
    #         turns.append(curr_pt)
    #     turns.append((dest_x, dest_y))
    #     return turns[0]
        #this is what goes for the main function
if __name__=='__main__':
    mat = [
        [0, 1, 1, 1, 1, 0, 0, 1, 1, 1],
        [0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
        [0, 0, 1, 0, 1, 1, 1, 0, 0, 1],
        [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
        [0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
        [1, 0, 1, 1, 1, 0, 0, 1, 1, 0],
        [0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
        [0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
        [1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
        [0, 0, 1, 0, 0, 1, 1, 0, 0, 1]
    ]            
    M=10
    N=10        
    algo=dfs(mat, M, N, 0, 0, 6, 2)
    algo.traversal()