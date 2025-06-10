import threading
import time

def hello_world(name):
    time.sleep(0.1)
    print(f"hello world!{name} executed on {threading.current_thread().name}")

t1= threading.Thread(target=hello_world, args = ('a',),name = 't1')  # creation of thread
t2 = threading.Thread(target=hello_world, args=('b',),name = 't2')  # creation of thread

t1.start()  # submit the thread to os scheduler
t2.start()   # submit the thread to os scheduler

hello_world("a")  # for this call, thread is not assigned. so it will be assigned to main thread
hello_world("b")  # if thread is not specified, it will assign the program to single thread only