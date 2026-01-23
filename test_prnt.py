import time
N = 100_000

a: int = 400
b: int = 50
c: int = 0
c = c*c
bl = a > b
i = int(a > b)

#Elágazással
def elag_prnt(b: int, ind: int) -> float:
    start = time.perf_counter()
    for i in range(N):
        if i % 10000 == 0:
            elagazas = i / 1000
#-------------------------------------
        if bl:
            print(f"[{ind}]: {a}\t-\t{elagazas=}%")
        else:
            print(b)
#-------------------------------------
    stop = time.perf_counter()
    return stop - start

#Ternary operátorral
def tern_prnt(a: int, b: int, ind: int) -> float:
    start = time.perf_counter()
    for i in range(N):
        if i % 10000 == 0:
            ternary = i / 1000
#-------------------------------------
        print(f"[{ind}]: {a}\t-\t{ternary=}%") if a > b else print(b)
#-------------------------------------
    stop = time.perf_counter()
    return stop - start

#Elágazás nélkül
def elnel_prnt(a: int, b: int, ind: int) -> float:
    start = time.perf_counter()
    for i in range(N):
        if i % 10000 == 0:
            branchless = i / 1000
#-------------------------------------
        print(f"[{ind}]: {a * (a>b) + b * (a<b)}\t-\t{branchless=}%")
#-------------------------------------
    stop = time.perf_counter()
    return stop - start
