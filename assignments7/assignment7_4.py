# Get thread id, name. Counte small, capital and digits of a string
import threading
import os
def small(string):
    print('name of ', str(threading.current_thread().name))
    print('thread id', threading.current_thread())
    count=0
    for i in string:
        if(i.islower()):
            count = count+1
    print(count)
def capital(string):
    print("name of ", str(threading.current_thread().name))
    print('thread id', threading.current_thread())
    count=0
    for i in string:
        if(i.isupper()):
            count = count+1
    print(count)
def digits(string):
    print("name of ", str(threading.current_thread().name))
    print("thread id ", str(threading.current_thread()))
    count=0
    for i in string:
        if(i.isdigit()):
            count = count+1
    print(count)
def main():
    print('main pid', os.getpid())
    print('main thread id', threading.current_thread())
    string = "Python programming for ML, assignment7"
    smallthread = threading.Thread(target=small, args=(string,))
    capitalthread = threading.Thread(target=capital, args=(string,))
    digitsthread = threading.Thread(target=digits, args=(string,))
    smallthread.start()
    capitalthread.start()
    digitsthread.start()
    smallthread.join()
    capitalthread.join()
    digitsthread.join()
if __name__ == "__main__":
    main()
