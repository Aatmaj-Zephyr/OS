C = [
   [25],
   [20],
   [45],
   [26]
]

A = [
   [45],[40],[15],[35]
]
R = [150] #total
V = [50] #avaiable
process = range(4)
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
        #print(V)
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
