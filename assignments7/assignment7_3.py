# Evenlist and oddlist sum threads
import threading
def evensum(n):
    s = 0
    for i in n:
        if i % 2 == 0:
            s = s+i
    print(s)
def oddsum(n):
    s = 0
    for i in n:
        if i % 2 != 0:
            s = s+i
    print(s)
def main():
    evenlist = threading.Thread(target=evensum, args=([18,13,45,78],))
    oddlist = threading.Thread(target=oddsum, args=([18,13,45,78],))
    evenlist.start()
    oddlist.start()
    evenlist.join()
    oddlist.join()
if __name__ == "__main__":
    main()
