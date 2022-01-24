# import numpy as np
from collections import deque
class dfs:
    def __init__(self,map,M,N,x_i,y_i,x_f,y_f):
        self.map=map
        self.M=M
        self.N=N
        self.visited=[[False for x in range(self.M)] for y in range(self.N)]
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
        self.next_pose_index=0
    
    def matrix_update(self,i,j):
        if (i,j,self.dist+1) not in self.q:
            self.q.append((i,j,self.dist+1))
            # #print(self.q)
        self.visited[i][j]=True
        # #print(self.visited)
        self.cost[i][j]=self.dist + 1
        # #print(self.cost)
    def isValid(self, row, col):
        return (row >= 0) and (row < self.M-1) and (col >= 0) and (col < self.N-1) \
            and self.map[row][col] == 0 and not self.visited[row][col]
 
    def free_node(self,i,j): #this will give me the priority of node to choose
        # 0 means free space
        # print(self.map)
        
        # print(len(self.map))
        i_prev=0
        j_prev=0
        min=0
        for k in range(4):
            i_neigh=i+self.row[k]
            j_neigh=j+self.col[k]
            # if i_neigh < 0 or j_neigh < 0 or i_neigh > self.M-1 or j_neigh > self.N-1:
            #     pass
            # if self.visited[i_neigh][j_neigh]:
            #     pass
            # checking for free space and is it a valid cell or not
            valid=self.isValid(i_neigh, j_neigh)
            if valid:    
                self.a[i_neigh][j_neigh]=abs((i_neigh+j_neigh)-(self.x_f+self.y_f))
                # #print(a[i][j])
                min=self.a[i_neigh][j_neigh]
        for l in range(4):
            i_neigh=i+self.row[l]
            j_neigh=j+self.col[l]
            # if i_neigh < 0 or j_neigh < 0 or i_neigh > self.M-1 or j_neigh > self.N-1:
            #     return
            # if self.visited[i_neigh][j_neigh]:
            #     return
            valid=self.isValid(i_neigh, j_neigh)
            if valid:
                if self.a[i_neigh][j_neigh]>min:
                    if (i_neigh,j_neigh) not in self.free_neigh:
                        self.free_neigh.appendleft((i,j))
                if self.a[i_neigh][j_neigh]<=min:
                    min=self.a[i_neigh][j_neigh]
                    if (i_neigh,j_neigh) not in self.free_neigh:
                        self.free_neigh.append((i_neigh,j_neigh)) #last added one has more importance than the before one so use only pop
                # #print(self.free_neigh) 
                # if len(self.free_neigh)!=0:
                #     (i_prev,j_prev)=self.free_neigh.pop()  
        # if len(self.free_neigh)==0 and (i,j)!=(self.x_f,self.y_f): 
        #     #back tracking is needed
        #     if len(self.route)!=0:
        #         self.route.pop()
        #     self.free_node(i_prev, j_prev)   
        # return int(i_next), int(j_next)
        

        
    def traversal(self):
        #i and j are the current nodes I am standing in
        i=self.x_i
        j=self.y_i
        i_next=0
        j_next=0
        i_prev=0
        j_prev=0 
        turns=[]
        self.next_pose_index+=1
        valid=True
        if len(self.free_neigh)==0 and (i,j)!=(self.x_f,self.y_f):     #when back tracking is needed
            valid=False
        while (i,j)!= (self.x_f,self.y_f):    
            self.matrix_update(i, j)
            self.free_node(i, j)
            #print(self.free_neigh)
            i_prev=0
            j_prev=0 
            # while self.free_neigh:
            
            if len(self.free_neigh)!=0:
                (i,j)=self.free_neigh.pop()
            else:
                #print("destination can't be reached from the given route back tracking is needed")
                break
            #print((i,j))
            
            if (i,j) not in self.route:
                self.route.append((i,j))
            i_prev=i
            j_prev=j  
            # if len(self.free_neigh)==0 and (i,j)!=(self.x_f,self.y_f):     
            #     break
        for i_ in range(1,len(self.route)-1):
            prev_pt = self.route[i_-1]
            curr_pt = self.route[i_]
            next_pt = self.route[i_+1]
            if prev_pt[0]!=next_pt[0] and prev_pt[1]!=next_pt[1]:
                (l,m)=self.route[i_]
                if (l,m) not in turns:
                    turns.append(curr_pt)
        turns.append((self.x_f, self.y_f))
        print(self.route)
        print(turns)
        print(turns[0])
        if i == self.x_f and j == self.y_f:
            self.min_dist = self.dist
            print("--------goal reached---------")
            # print(self.route)
            print(turns)
            turn_1=turns[0]
            return turns[0]     
            # self.route.pop()
            # #print(self.route)
            # self.traversal()
        if self.min_dist == float('inf'):
            print("Destination can't be reached from given source")
            return -1
        
        
        # return final_value
    
    # def path(self):
    #     if self.min_dist == float('inf'):
    #         #print("Destination can't be reached from given source")
    #         return -1
        
    #     #print("The shortest path from source to destination has length", self.min_dist)
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
# if __name__=='__main__':
#     mat = [
#         [0, 0, 0, 1, 1, 0, 0, 1, 1, 1],
#         [1, 1, 0, 1, 1, 1, 0, 1, 0, 1],
#         [0, 0, 0, 0, 1, 1, 1, 0, 0, 1],
#         [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
#         [0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
#         [1, 0, 1, 1, 1, 0, 0, 1, 1, 0],
#         [0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
#         [0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
#         [1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
#         [0, 0, 1, 0, 0, 1, 1, 0, 0, 1]
#     ]            
#     M=10
#     N=10        
#     algo=dfs(mat, M, N, 0, 0, 7, 0)
#     a=algo.traversal()
#     #print(a)