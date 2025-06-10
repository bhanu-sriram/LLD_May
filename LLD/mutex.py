import threading

mutex = threading.Lock()
a =0
def add():
    global a
    for i in range(100000):
        a+=1

def sub():
    global a
    for i in range(100000):
        a-= 1

t1 = threading.Thread(target=add)
t2 = threading.Thread(target=sub)

t1.start()
t2.start()

t1.join()
t2.join()
print(a)