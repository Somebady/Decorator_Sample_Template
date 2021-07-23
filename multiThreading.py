from timeit import default_timer as timer
from threading import Thread,Lock,current_thread
import os
import time
value=0

# def func(n: int,lock):
#     global value
#     # lock.acquire()
#     # Either use a lock or a semaphore to ensure that the value is not overridden at same time
#     with lock:
#         for i in range(n):
#             print(current_thread().name, i*i,end=' ')
#             # time.sleep(0.1)
#             # print(timer())
#     # lock.release()

# if __name__ == '__main__':

#     thread=[]
#     num_th=100
#     lock=Lock()
#     for i in range(num_th):
#         t=Thread(target=func,args=(10,lock))
#         t._deamon=True
#         t.start()
#     # for t in thread:
#     #     t.join()
#     # print(value)
#     print('enddddddddddd')

# Write sample programe to demonstarte the use of threading module
import threading
import time

def worker():
    print(threading.currentThread().getName(), 'Starting')
    time.sleep(2)
    print(threading.currentThread().getName(), 'Exiting')

def my_service():
    print(threading.currentThread().getName(), 'Starting')
    time.sleep(3)
    print(threading.currentThread().getName(), 'Exiting')

t = threading.Thread(name='my_service', target=my_service)
w = threading.Thread(name='worker', target=worker)
w2 = threading.Thread(target=worker) # use default name

w.start()
w2.start()
t.start()

#
# # Output:
# # worker Starting
# # worker Exiting
# # my_service Starting
# # worker Exiting
# # my_service Exiting
#
#

