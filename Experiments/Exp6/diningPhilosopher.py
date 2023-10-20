
import time
import threading
import random
chopSticks = [threading.Lock() for i in range(5+1)]
philosopherStates = [0,0,0,0,0,0]
printer = threading.Lock()
class philosopher():
   
    def __init__(self,name):
        self.name=name
        self.state=0
        philosopherStates[self.name]=0
    
    """
    0 - Thinking
    1 - Hungry
    2 - Eating
    """
    def run(self):
        for i in range(2):
            self.think()
            self.take_fork()
            self.eat()
            self.put_fork()
    def think(self):
        self.state = 0
        philosopherStates[self.name]=0
        time.sleep(random.random())
    def eat(self):
        self.state=2
        philosopherStates[self.name]=2
        printer.acquire()
        print("philosopher ", self.name, "is eating.")
        printer.release()
    def put_fork(self):
        chopSticks[self.name].release()
        printer.acquire()
        print("philosopher ", self.name, "has dropped up left stick")
        printer.release()
        
        chopSticks[(self.name+1) %5].release()
        printer.acquire()
        print("philosopher ", self.name, "has dropped up right stick")
        printer.release()

    def take_fork(self):
        self.state = 1
        philosopherStates[self.name]=1
        printer.acquire()
        print("philosopher ", self.name, "is hungry.")
        printer.release()
        while True:
            if(philosopherStates[self.name]!=2 and philosopherStates[(self.name+1) % 5]!=2 ): # if philosopher i is hungry and both neighbours are not eating then eat
                chopSticks[self.name].acquire()
                chopSticks[(self.name+1) % 5].acquire()
                printer.acquire()
                print("philosopher ", self.name, "has picked up sticks ")
                printer.release()
                break
                
            

philosopher1=philosopher(1)
philosopher2=philosopher(2)
philosopher3=philosopher(3)
philosopher4=philosopher(4)
philosopher5=philosopher(5)



T1 = threading.Thread(target = philosopher1.run,args=())
T2 = threading.Thread(target = philosopher2.run,args=())
T3 = threading.Thread(target = philosopher3.run,args=())
T4 = threading.Thread(target = philosopher4.run,args=())
T5 = threading.Thread(target = philosopher5.run,args=())
T1.start()
T2.start()
T3.start()
T4.start()
T5.start()