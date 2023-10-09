# function to simulate reader writer
import time
max_len = 10
def writer(n,mutex,pointer):
    for i in range(10):
            if(pointer.value<max_len):
                
                if   (mutex.value==0):
                    mutex.value = 1 #flop
                    pointer.value+=1
                    n[pointer.value]=1
                    print("I am writing at",pointer.value )
                    for i in n:
                          print(i,end=",")
                    print()
                mutex.value = 0 #flop

                
            time.sleep(0.2)

def reader(n,mutex,readerno):
    for i in range(10):
         
        if   (mutex.value==0):
            mutex.value = 1 #flip
            print("Reader no ", readerno,"reads ",end="")
            for i in n:
                        print(i,end=",")
            print()

        mutex.value = 0 #flip
        time.sleep(0.3+readerno*0.2)

                
if __name__ == '__main__': # dont remove this line code wont run in windows.
    import multiprocessing

    # Define a shared variable
    n =  multiprocessing.Array('i', max_len)
    mutex = multiprocessing.Value('i',0)
    pointer = multiprocessing.Value('i',-1)

   

    # Create two processes that run the increment function
    process1 = multiprocessing.Process(target=writer,args=(n,mutex,pointer,))
    process2 = multiprocessing.Process(target=reader,args=(n,mutex,1,))
    process3 = multiprocessing.Process(target=reader,args=(n,mutex,2,))

    # Start both processes
    process1.start()
    process2.start()
    process3.start()

    
    
