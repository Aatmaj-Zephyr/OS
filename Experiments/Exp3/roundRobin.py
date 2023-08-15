k=int(input("Please enter number of processes "))

arrivalTime=[int(input("Please enter arrival time for process "+str(i)+" ")) for i in range(k)]

reqTime=[int(input("Please enter estimated time for process "+str(i)+" ")) for i in range(k)]

processes=range(k)
timeQuantaDecided =int(input("Please enter the time quanta "))

'''
#Test case 

arrivalTime=[0,1,3,2]
reqTime=[8,4,2,3]
processes=[0,1,2,3]
timeQuantaDecided =2

'''

timeQuanta = timeQuantaDecided
queue=[]
answer=[]
for i in range(100):
    
    for process in processes: #check new processes comming
        if(arrivalTime[process]==i):
            queue.append(process)
    if(reqTime[queue[0]]==0):# if process still over next
            timeQuanta= timeQuantaDecided
            queue.pop(0)
    elif(timeQuanta==0):
        timeQuanta= timeQuantaDecided
        queue.append(queue[0])
        queue.pop(0)
        
    if(len(queue)==0 and i!=0):
         break
    currentProcess=queue[0]
    print(i,"\t", currentProcess,"\t\t\t",queue)
    
   
    answer.append(currentProcess)
    reqTime[currentProcess]-=1
    timeQuanta-=1 
     
print("\n")    
print("\n_____________________________________________________________________________________________________________________________________________________")

temp=-1
for i in range(0,len(answer)):
    if(i==0): 
        print("|",answer[i],end="\t")
        temp=answer[i]
    else:
        if(temp==answer[i]):
             print("", end="\t")
             continue
        else:
             print("|",answer[i],end="\t")
             temp=answer[i]
print("|\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------")
for i in range(0,len(answer)+1):
     print(i,end="\t")

        
        
