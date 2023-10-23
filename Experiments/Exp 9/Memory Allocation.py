memory = [0 for i in range(32)]
pointer = 0
def nextFit(memory, process_size,pointer):
    for ptr in range(pointer, pointer + len(memory)):
        ptr = ptr % len(memory)
        if(ptr + process_size > len(memory)):
            continue
        if(sum(memory[ptr : ptr + process_size]) == 0): # is all 0
            #allocate
            print(ptr)
            for i in range(ptr , ptr + process_size):
                memory[i] = 1
                
            return (memory,ptr + process_size)

    print("memory full")
    return -1

def firstFit(memory, process_size,pointer):
    nextFit(memory, process_size,0)
    

def bestFit(memory, process_size,pointer):
    memarray = []
    memscore = []
    ptr = 0
    while(True):
        mem,ptr = nextFit(memory.copy(), process_size,ptr)
        score = 0
        if(mem in memarray):
            break # repeat reached
        for i in range(ptr,len(mem)):
            if(mem[i]==0):
                score +=1
            else:
                break
        memarray.append(mem)
        memscore.append(score)
        print(memscore)
        memory = memarray[memscore.index(min(memscore))]
        return memarray[memscore.index(min(memscore))]
        
#randomly fill array
nextFit(memory,2,pointer)
nextFit(memory,3,pointer+3)
nextFit(memory,2,pointer+8)
nextFit(memory,4,pointer+17)
nextFit(memory,5,pointer+13)
print(memory)
#[1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0]
pointer = 4 
nextFit(memory,6,pointer)
print(memory)
#[1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0]
pointer = 5

firstFit(memory,1,pointer)
print(memory)
#[1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0]
memory = [0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0]
bestFit(memory,2,pointer)
print(memory)
