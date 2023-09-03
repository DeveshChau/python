# Evenfactors and oddfactors sum threads
import threading
def evenfactorssum(n):
    s = 0
    for i in range(1, n+1):
        if n % i == 0:
            if i % 2 == 0:
                s = s+i
    print(s)
def oddfactorssum(n):
    s = 0
    for i in range(1, n+1):
        if n % i == 0:
            if i % 2 != 0:
                s = s+i
    print(s)
def main():
    evenfactor = threading.Thread(target=evenfactorssum, args=(18,))
    oddfactor = threading.Thread(target=oddfactorssum, args=(18,))
    evenfactor.start()
    oddfactor.start()
    evenfactor.join()
    oddfactor.join()
    print("exit from main")
if __name__ == "__main__":
    main()
