import time

def usingWhile():
    j = 0 
    while j<50000:
        j = j+1
        print(j) 

def usingFor():
    for j in range(50000):
        print(j) 
        
init = time.time()
        
usingFor()  
t1 = time.time() - init 
init = time.time()
usingWhile()
print(time.time() - init) 
print(t1)