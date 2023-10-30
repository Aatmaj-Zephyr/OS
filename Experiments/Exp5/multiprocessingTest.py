# function to demonstrate how sharing a value can lead to chaos

import time
 # Function to increment the shared variable
def increment(n):
        
        for _ in range(10 ):
             
                n.value += 1
                print(n.value)
                time.sleep(0.2)

 # Function to multiply the shared variable
def multiply(n):
        
        for _ in range(10 ):
             
                n.value *= 2
                print(n.value)
                time.sleep(0.3)
                
if __name__ == '__main__': # dont remove this line code wont run in windows.
    import multiprocessing

    # Define a shared variable
    n = multiprocessing.Value('i', 0)

   

    # Create two processes that run the increment function
    process1 = multiprocessing.Process(target=increment,args=(n,))
    process2 = multiprocessing.Process(target=multiply,args=(n,))

    # Start both processes
    process1.start()
    process2.start()

    
    
