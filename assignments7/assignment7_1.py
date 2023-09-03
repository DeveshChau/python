# Even and odd threads
import threading
def evenNum():
    for i in range(2,21,2):
        print(i)
def oddNum():
    for i in range(1,22,2):
        print(i) 
def main():
    even = threading.Thread(target=evenNum)
    odd = threading.Thread(target=oddNum)
    even.start()
    odd.start()
    even.join()
    odd.join()
if __name__ == "__main__":
    main()
