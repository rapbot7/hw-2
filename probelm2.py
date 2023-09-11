import numpy as np
class node:
        x=0
        y=0        
        parent_cost=[]
        index=[]
        def __init__(self,x,y,parent_cost,index):
             self.x = x
             self.y = y
             self.parent_cost=parent_cost
             self.index=index

def is_valid(a:node,obstacle_list:tuple,obs_diameter:float,x_max:float,y_max:float,x_min:float,y_min:float,step:float):
    if a.x > x_max or a.x < x_min or a.y > y_max or a.y < y_min:
         return False
    
    if a.x % step !=0 or a.y % step !=0:
         return False

    for obs in obstacle_list:
             dist = np.sqrt((a.x-obs[0])**2+(a.y-obs[1])**2)
             if dist<obs_diameter/2:
                   return False
             
    return True
if __name__=='__main__':
 
# test the obstale list
 obstcale_list=( (1,1), (4,4), (3,4), (5,0), (5,1), (0,7), (1,7), (2,7), (3,7) )    
dia=0.5
step=0.5
x_min=0
y_min=0
x_max=10
y_max=10
test_node=node(-0.5,-0.5,0,0)
bool=is_valid(test_node,obstcale_list,0.5,10,10,0,0,0.5)

print(bool)

# this is for the problem2 of the homework-2 :)

       
    
