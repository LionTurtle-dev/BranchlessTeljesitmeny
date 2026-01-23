import time
N = 100_000

a: int = 400
b: int = 50
c: int = 0
bl = a > b
i = int(a > b)

#Elágazással
def elag_bsc(a: int) -> float:
    start = time.perf_counter()
    for i in range(N):
        if i % 10000 == 0:
            elagazas = i / 1000
            print(f"{elagazas=}%")
        #Alap elágazás
#-------------------------------------
        if bl: #a > b
            a = 400
        else:
            a = 500
#-------------------------------------
    stop = time.perf_counter()
    return stop - start

#Ternary operátorral
def tern_bsc(a: int, b: int) -> float:
    start = time.perf_counter()
    for i in range(N):
        if i % 10000 == 0:
            ternary = i / 1000
            print(f"{ternary=}%")
        #Ternary operátor
#-------------------------------------
        a = 400 if a > b else 500
#-------------------------------------
    stop = time.perf_counter()
    return stop - start

#Elágazás nélkül
def elnel_bsc(a: int, b: int, c: int) -> float:
    start = time.perf_counter()
    for i in range(N):
        if i % 10000 == 0:
            branchless = i / 1000
            print(f"{branchless=}%")
#-------------------------------------
        c = a * (a>b) + b * (a<b) 
        #a=400, b=50 -> (a>b) = 1 (a<b) = 0
        #a = 400×1+50*0 -> 400
#-------------------------------------
    stop = time.perf_counter()
    return stop - start
