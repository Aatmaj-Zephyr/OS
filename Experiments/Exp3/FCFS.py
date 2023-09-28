
k=int(input("Please enter number of processes "))

arrivalTime=[int(input("Please enter arrival time for process "+str(i)+" ")) for i in range(k)]

reqTime=[int(input("Please enter estimated time for process "+str(i)+" ")) for i in range(k)]


timeQuantaDecided =20000

'''
#Test case 

k=5
arrivalTime=[0,2,4,6,7]
reqTime=[2,3,4,5,6]
timeQuantaDecided =2000
'''
processes=range(k)
timeQuanta = timeQuantaDecided
reqTimeCopy=[i for i in reqTime]
queue=[]
answer=[]
waiting=[0 for i in range(k)]

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
    
    for waitingProcess in processes:
        # if process arrived and waiting and present in queue(not terminated)
        if(waitingProcess!=currentProcess and arrivalTime[waitingProcess]<=i and waitingProcess in queue):
            waiting[waitingProcess]+=1
    answer.append(currentProcess)
    reqTime[currentProcess]-=1
    timeQuanta-=1 
    
    
print("Total time spent waiting for processes is given by", waiting) 
print("Average waiting Time",sum(waiting)/len(waiting))
turnaroundTimeArray=[int(waiting[i])+int(reqTimeCopy[i]) for i in processes]
print("Total turnaround time for processes is given by",turnaroundTimeArray )
print("Average turnaround Time",sum(turnaroundTimeArray)/len(turnaroundTimeArray))     
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
