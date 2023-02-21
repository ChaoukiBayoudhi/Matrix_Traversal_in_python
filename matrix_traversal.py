#return a row from a matrix
import random
import numpy as np

class Matrix:
    #constructor
    def __init__(self,M,n=0):
        if n==0:
            self.M=M
        else:
            #generate a matrix using np package
            #it gives a matrix like
            # [[ 1  2  3  4  5],[ 6  7  8  9 10],[11 12 13 14 15]]
            #self.M=np.random.randint(1,100,size=(n,n))
            #generate a matrix using random package
            #it gives a matrix as a list of list like
            #[[49, 43, 9, 44, 96], [45, 50, 87, 61, 76], [56, 90, 84, 34, 66]]
            self.M=[[random.randint(1,100) for i in range(n)]for j in range(n)]
 
    def showMatrix(self):
        print(self.M)
        
    def getRow(self,index):
        return self.M[index]
    
    def getColumn(self,index):
        return [X[index] for X in self.M]
    
    def getDiagonal(self,choice):
        D=[]
        try:
            if choice==1:
                for i in range(len(self.M)):
                    D.append(self.M[i][i])
            elif choice==2:
                for i in range(len(self.M)):
                    D.append(self.M[i][len(self.M)-i-1])
            else:
                raise ValueError ("Invalid choice")        
        except ValueError as e:
            print(e)
        return D
    def spiralTraversal(self,):
        n=len(self.M)
        if n==0:
            return []
        TS=[]
        
        left=0
        right=n
        top=0
        bottom=n
        while left<right and top<bottom:
            for i in range(left,right):
                TS.append(self.M[top][i])
            top+=1
            for i in range(top,bottom):
                TS.append(self.M[i][right-1])
            right-=1
            for i in range(right-1,left-1,-1):
                TS.append(self.M[bottom-1][i])
            bottom-=1
            for i in range(bottom-1,top-1,-1):
                TS.append(self.M[i][left])
            left+=1
        return TS

                
    def spiral_traverse(self,):
        result = []
        while self.M:
            result += self.M.pop(0)
            if self.M and self.M[0]:
                for row in self.M:
                    result.append(row.pop())
            if self.M:
                result += self.M.pop()[::-1]
            if self.M and self.M[0]:
                for row in self.M[::-1]:
                    result.append(row.pop(0))
        return result

    def generateMatrix(self,):
        self.M=np.random.randint(1,100,size=(5,5))



#Execution
#instantiation
#m1=Matrix([[1,2,3],[4,5,6],[7,8,9],])

n=int(input('Matrix size: '))
m1=Matrix([],n)
indexL=int(input('Enter the row index'))
print(m1.getRow(indexL))
indexC=int(input('Enter the column index'))
print(m1.getColumn(indexC))
print('principal diagonal :')
print(m1.getDiagonal(1))
print('Second diagonal :')
print(m1.getDiagonal(1))
print('The Matrix is :')
m1.showMatrix()

print('Matrix traversal :')
print(m1.spiralTraversal())
print('Matrix traversal :')

print(m1.spiral_traverse())
