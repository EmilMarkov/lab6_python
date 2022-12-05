import os.path
from time import time
from threading import Thread

def generate(N):
    for i in range(N):
        fp = open(f"txts\{i}_abc.txt", "w+")
        fp.close()
        fp1 = open(f"txts1\{i}_abcc.txt", "w+")
        fp1.close()
        fp2 = open(f"txts2\{i}_abccc.txt", "w+")
        fp2.close()

def find_files():
    for dirpath, dirnames, filenames in os.walk("."):
        for filename in [f for f in filenames if f.endswith(".txt")]:
            if (os.path.join(dirpath, filename).find("abcc")):
                t = open(os.path.join(dirpath, filename))
                t.close()

generate(3000)

start = time()
find_files()
find_files()
print("With 1 thread: " + str(time() - start) + " seconds")

start = time()
t1 = Thread(target=find_files)
t1.start()
t2 = Thread(target=find_files)
t2.start()
t1.join()
t2.join()
print("With 2 threads: " + str(time() - start) + " seconds")