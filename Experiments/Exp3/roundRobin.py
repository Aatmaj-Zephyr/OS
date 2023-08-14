arrivalTime=[0,1,3,2]
reqTime=[8,4,2,3]
processes=[0,1,2,3]
timeQuantaDecided =2
timeQuanta = timeQuantaDecided
queue=[]
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
    print(i,"",queue,end="....")
    print(currentProcess)
    reqTime[currentProcess]-=1
    timeQuanta-=1 
     
    
    
   
        
        
