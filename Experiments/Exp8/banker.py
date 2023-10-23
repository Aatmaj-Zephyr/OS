C = [
   [3,2,2],
   [6,1,3],
   [3,1,4],
   [4,2,2]
]

A = [
   [1,0,0],
   [6,1,2],
   [2,1,1],
   [0,0,2]
]
R = [3,3,2] #total
V = [0,1,1] #avaiable
process = range(5)
import numpy as np
A = np.array(A)
C = np.array(C)
R = np.array(R)
V = np.array(V)
process = np.array(process)
D = C - A

while(len(D)!=0):
    index = -1
    terminate = True
    for i in D:
        index +=1
        print(V)
        if((i <= V).all()):
            print("process ", process[index], " can continue")
            V = V + A[index]
            C=np.delete(C, index, axis=0)
            A=np.delete(A, index, axis=0)
            D=np.delete(D, index, axis=0)
            process = np.delete(process,index,axis = 0)
            terminate = False
            if(len(process)==0):
                exit
            break
    if(terminate ==True):       
        print("Non safe state")
        break
    continue
