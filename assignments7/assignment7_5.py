# use of notify wait for thread schueduling
import threading
def incremental(condition_obj):
    condition_obj.acquire()
    for i in range(1,51):
        print(i)
    condition_obj.notify()
    condition_obj.release()
def decremental(condition_obj):
    condition_obj.acquire()
    condition_obj.wait()
    for i in range(50,0,-1):
        print(i) 
    condition_obj.release()
def main():
    condition_obj = threading.Condition()
    thread1 = threading.Thread(target=decremental, args=(condition_obj,))
    thread2 = threading.Thread(target=incremental, args=(condition_obj,))
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
if __name__ == "__main__":
    main()
