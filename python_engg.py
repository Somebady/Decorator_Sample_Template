from timeit import default_timer as timer
from multiprocessing import Process
import os
import time
# if __name__ == '__main__':

#     def func(n):
#         for i in range(n):
#             print(i*i,end=' ')
#             print(timer())
#             time.sleep(0.1)
#     processes=[]
#     num_proceses=os.cpu_count()

#     for p in range(num_proceses):
#         p = Process(target=func(10),args=(10,))
#         processes.append(p)

#     for p in processes:
#         p.start()
        

#     for p in processes:
#         p.join()

#     print('enddddddddddd')


 # Who are you?
 # I'm a process.
 # I'm a process.
 # I'm a process.


 # How to Revise python Flask app
 # 1. Change the code to use a class
 # 2. Add a route to the flask app
 # 3. Add a static folder to the flask app
 # 4. Add a route to serve the static folder
 # 5. Add a route to serve the index.html file
 # 6. Add a route to serve the style.css file
 # 7. Add a route to serve the javascript file
 # 8. Add a route to serve the main.js file
 # 9. Add a route to serve the index.html file

x=11
assert x>10

print(x)
lst=[i for i in range (0,10000)]
print(lst.__sizeof__())

lst2=(i for i in range (0,10000000))
print(lst2.__sizeof__())
print(type(lst2))
lst1=iter(lst)
print(lst1.__sizeof__())

def fun():
    yield from range(1000)
x=fun()
print(type(x))
print(x.__sizeof__())




