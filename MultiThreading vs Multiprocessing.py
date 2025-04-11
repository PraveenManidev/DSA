import multiprocessing
import time 

def worker(num):
    print(f"Worker{num} has started")
    time.sleep(2)
    print(f"Worker{num} has ended")

if __name__ == '__main__':
    processes = []

    for i in range(4):
        p = multiprocessing.Process(target=worker,args=(i,))
        p.start()
        processes.append(p)
    
    for p in processes:
        p.join()
    print("All process completed")

'''import threading
import time

ls = []

def count(n):
    for i in range(n):
        ls.append(i)
        time.sleep(0.5)

def count2(n):
    for i in range(n):
        ls.append(i)
        time.sleep(0.5)

x = threading.Thread(target=count,args=(10,))
y = threading.Thread(target=count2, args=(10,))
x.start()
x.join()
y.start()

y.join()
print(ls)'''