'''
SJF (non preemptive)
k=int(input("Please enter number of processes "))

arrivalTime=[int(input("Please enter arrival time for process "+str(i)+" ")) for i in range(k)]

reqTime=[int(input("Please enter estimated time for process "+str(i)+" ")) for i in range(k)]


priority=[int(input("Please enter priority for process "+str(i)+" ")) for i in range(k)]



'''
#Test case 

k=5
arrivalTime=[0,2,4,6,7]
reqTime=[2,3,4,5,6]
priority=[3,2,1,4,5]


processes=range(k)

reqTimeCopy=[i for i in reqTime]
queue=[]
answer=[]
waiting=[0 for i in range(k)]

for i in range(100):
    
    for process in processes: #check new processes comming
        if(arrivalTime[process]==i):
            queue.append(process)
            if(len(queue)==1): # for first process
                 currentProcess=process 
    if(reqTime[queue[0]]==0):# if process ended, then only go to next process
            queue.pop(0)
            if(len(queue)==0 and i!=0):
                 break # all processes over
            currentProcess = reqTime.index(min([reqTime[process] for process in range(len(processes)) if process in queue]))
            queue.remove(currentProcess)
            queue.insert(0,currentProcess)
    
        
    if(len(queue)==0 and i!=0):
        break # all processes over
    
    
    currentProcess = currentProcess # non preemptive 

    print(i,"\t", currentProcess,"\t\t\t",queue)
    
    for waitingProcess in processes:
        # if process arrived and waiting and present in queue(not terminated)
        if(waitingProcess!=currentProcess and arrivalTime[waitingProcess]<=i and waitingProcess in queue):
            waiting[waitingProcess]+=1
    answer.append(currentProcess)
    reqTime[currentProcess]-=1

    
print("Total time spent waiting for processes is given by", waiting) 
print("Total turnaround time for processes is given by", [int(waiting[i])+int(reqTimeCopy[i]) for i in processes])      
print("\n")    
print("\n_________________________________________________________________________________________________________________________________________________________________")

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
