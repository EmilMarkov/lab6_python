import time
import math
from random import randint
from multiprocessing import Process

N = 5000

def calc(p, q):
    return round(math.sqrt(abs(q - p)))

def worker(P, Q, N):
    matrix = []
    print(P)
    for i in range(N // 5):
        ls = []
        for j in range(N // 5):
            ls.append(calc(P[i], Q[i]))
        matrix.append(ls)

if __name__ == "__main__":
    P = []
    Q = []
    ps = []
    nn = 0 # текущий индекс

    for i in range(N):
        P.append(randint(1, N))
        Q.append(randint(1, N))

    # Multi
    start = time.time()
    for _ in range(5):
        ps.append(Process(target = worker, args = (P[nn::5], Q[nn::5], N), name = f"Process {_}"))
        ps[_].start()
        nn += 1
    for item in ps:
        item.join()
    print(f"Multiprocess: {round(time.time() - start, 5)} seconds")

    # Single
    start = time.time()
    worker(P, Q, N * 5)
    print(f"Single process: {round(time.time() - start, 5)} seconds")