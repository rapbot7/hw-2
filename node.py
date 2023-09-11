class node:
        x=[]
        y=[]
        parent_cost=[]
        index=[]
        def __init__(self,x,y,parent_cost,index):
             self.x = x
             self.y = y
             self.parent_cost=parent_cost
             self.index=index

import numpy as np
def compute_dist(a:node,b:node):
       return np.sqrt((a.x-b.x)**2+(a.y-b.y)**2)

if __name__=='__main__':
 # test the distance of (2,1) and (3,2)

 a=node(2,1,0,0)
 b=node(3,2,0,0)

 dist=compute_dist(a,b)

 print(dist)

#this is for the problem-1 of homework-2