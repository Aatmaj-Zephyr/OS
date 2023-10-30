num = 10

#num = int(input("please enter number of values "))
tasks_input = [98, 183, 37, 122, 14, 124, 65, 67.]

#tasks_input = [int(input("please enter sectors ")) for i in range(num)]


def calculateSeekTime(tasks):

    time = 0

    for i in range(len(tasks)-1):

        time += abs(tasks[i+1]-tasks[i])
        #print(time)

    time = time/ len(tasks)

    print("average time = ",time)
    return time

def FCFS(tasks):
    #print(tasks)

    calculateSeekTime(tasks)
    return tasks


def SCAN(tasks):

    answer = []


    #run loop over to check new tasks 
    # check new tasks
    initial = tasks[0] # last position of reader

    less = [i for i in tasks if i >= initial]

    less.sort()

    answer = answer + less

    for i in less:
        tasks.remove(i)
    ######check more tasks arrived in future

    # move down 
    

    
    tasks.sort()
    answer = answer +tasks[::-1]
    tasks = []

    #loop end 
    #print(answer)

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
    #print(answer)


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
    #print(answer)

    calculateSeekTime(answer)
    return answer


print(FCFS(tasks_input.copy()))

print(SSTN(tasks_input.copy()))

print(SCAN(tasks_input.copy()))

print(SCAN_C(tasks_input.copy()))
