num = 5
#num = int(input("please enter number of values"))
tasks = [3,1,2,5,6,4]
#tasks = [int(input("please enter sectors") for i in range(num))]

def calculateSeekTime(tasks):
    time = 0
    for i in range(len(tasks)-1):
        time += abs(tasks[i+1]-tasks[i])
        print(time)
    time = time/ len(tasks)
    print("average time = ",time)
    return time
def FCFS(tasks):
    print(tasks)
    calculateSeekTime(tasks)
    return tasks

def SCAN(tasks):
    answer = []

    #run loop over to check new tasks 
    initial = tasks[0] # last position of reader
    less = [i for i in tasks if i >= initial]
    less.sort()
    ######check more tasks arrived in future
    answer = answer + less
    more = [i for i in tasks if i < initial]
    more.sort()
    answer = answer + more
    print(answer)
    calculateSeekTime(answer)
    return answer

def SCAN_C(tasks):
    answer = []
    
    
    initial = tasks[0] # last position of reader
    less = [i for i in tasks if i >= initial]
    less.sort()
    answer = answer + less
    
    for i in less:
      tasks.remove(i)

    ###### check more tasks arrived in future
    #run loop over to check new tasks 
    tasks.sort()
    answer = answer + tasks
    print(answer)

    calculateSeekTime(answer)
    return answer

def SSTN(tasks):
    initial = tasks[0] # last position of reader
    answer = []
    answer.append(initial)
    while len(tasks):
        tasks.remove(initial)
        if(len(tasks) == 0):
            break
        minDifference = 10000
        minTask = -1
        for i in tasks:
            if(abs(i - initial)<minDifference):
                minDifference = abs(i - initial)
                minTask = i
        answer.append(minTask)
        #print(answer)
        initial = minTask 
        #print(initial)
    print(answer)
    calculateSeekTime(answer)
    return answer


SSTN(tasks)