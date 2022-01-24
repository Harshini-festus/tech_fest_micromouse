# Python3 program to solve Rat in a Maze
# problem using backracking
# from collections import deque
# Maze size
# A utility function to print solution matrix sol
class back_track_algo:
    def __init__(self,map,x_i,y_i,x_f,y_f,M,N):
        self.map=map
        self.M=M
        self.N=N
        self.x_i=x_i
        self.y_i=y_i
        self.x_f=x_f
        self.y_f=y_f
        self.q=[]
        self.sol = [ [ 0 for j in range(self.N) ] for i in range(self.M) ]
    def printSolution(self):
        for i in range(self.M):
            for j in range(self.N):
                if self.sol[i][j]==1:
                    self.q.append((i,j))
        print(self.q)    
    # A utility function to check if x, y is valid
    # index for N * N Maze

    def isSafe( self, x, y ):
        if x >= 0 and x < self.M and y >= 0 and y < self.N and self.map[x][y] == 0:
            return True
        return False

    """ This function solves the Maze problem using Backtracking.
        It mainly uses solveMazeUtil() to solve the problem. It
        returns false if no path is possible, otherwise return
        true and prints the path in the form of 1s. Please note
        that there may be more than one solutions, this function
        prints one of the feasable solutions. """

    def solveMaze(self):
        # Creating a 4 * 4 2-D list
        if self.solveMazeUtil(self.x_i, self.y_i) == False:
            print("Solution doesn't exist")
            return False
        self.printSolution()
        return True

        
    # A recursive utility function to solve Maze problem
    def solveMazeUtil(self,x, y):
        
        # if (x, y is goal) return True
        if x == self.N - 1 and y == self.N - 1 and self.map[x][y]== 0:
                self.sol[x][y] = 1
                # q.append((x,y))
                return True
        
            
        # Check if maze[x][y] is valid
        if self.isSafe(x, y) == True:
            # Check if the current block is already part of solution path.
            if self.sol[x][y] == 1:
                return False
            
            # mark x, y as part of solution path
            self.sol[x][y] = 1
            
            # Move forward in x direction
            if self.solveMazeUtil(x + 1, y) == True:
                return True
                
            # If moving in x direction doesn't give solution
            # then Move down in y direction
            if self.solveMazeUtil(x, y + 1) == True:
                return True
            
            # If moving in y direction doesn't give solution then
            # Move back in x direction
            if self.solveMazeUtil(x - 1, y) == True:
                return True
                
            # If moving in backwards in x direction doesn't give solution
            # then Move upwards in y direction
            if self.solveMazeUtil( x, y - 1) == True:
                return True
            
            # If none of the above movements work then
            # BACKTRACK: unmark x, y as part of solution path
            self.sol[x][y] = 0
            return False
    def final_callback(self):
        self.solveMaze()
        return self.q[0]

# Driver program to test above function
if __name__ == "__main__":
	# Initialising the maze
    maze =[ [0, 0, 0, 1, 1, 0, 0, 1, 1, 1],
            [1, 1, 0, 1, 1, 1, 0, 1, 0, 1],
            [0, 0, 0, 0, 1, 1, 1, 0, 0, 1],
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
    solver=back_track_algo(maze, 0, 0, 0, 3, M, N)
    solver.solveMaze()


