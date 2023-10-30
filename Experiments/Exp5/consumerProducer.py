# function to simulate consumer producer
import time
max_len = 10
def produce(n,mutex,pointer):
    for i in range(10):
            if(pointer.value<max_len):
                
                if   (mutex.value==0):
                    mutex.value = 1 #flop
                    pointer.value+=1
                    n[pointer.value]=1
                    print("I am producing at",pointer.value )
                    for i in n:
                          print(i,end=",")
                    print()
                mutex.value = 0 #flop
            else:
                print("Producer cannot produce at full array")
                
            time.sleep(0.2)

def consume(n,mutex,pointer):
    for i in range(10):
        if(pointer.value>=0):
            if   (mutex.value==0):
                mutex.value = 1 #flip
                n[pointer.value]=0
                print("I am consuming at" ,pointer.value)
                for i in n:
                          print(i,end=",")
                print()
                pointer.value-=1

            mutex.value = 0 #flip
        else:
            print("Consumer cannot consume from empty array")
        time.sleep(0.5)

                
if __name__ == '__main__': # dont remove this line code wont run in windows.
    import multiprocessing

    # Define a shared variable
    n =  multiprocessing.Array('i', max_len)
    mutex = multiprocessing.Value('i',0)
    pointer = multiprocessing.Value('i',-1)

   

    # Create two processes that run the increment function
    process1 = multiprocessing.Process(target=produce,args=(n,mutex,pointer,))
    process2 = multiprocessing.Process(target=consume,args=(n,mutex,pointer,))

    # Start both processes
    process2.start()
    process1.start()
    process2.join()
    process1.join()

    
    
