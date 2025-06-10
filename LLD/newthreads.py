import threading
import time

def hello_word():
    time.sleep(1)
    print(f"hello word executed on {threading.current_thread().name} at {time.ctime()}")

thread1 = threading.Thread(target=hello_word, name="thread1")
thread2 = threading.Thread(target=hello_word, name="thread2")
thread1.start()
thread2.start()
           