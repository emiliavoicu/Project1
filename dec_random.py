import random
import time

def dec_dif_time(func):
    def dormi(x):
        start=time.time()
        result=func(x)
        print 'a durat:', time.time()-start
        return result
    return dormi 

@dec_dif_time
def patrat(x):
    a=random.random()
    print 'o sa astept', a
    time.sleep(a)
    for i in range(10):
        x=x+1
    return x*x
    
print patrat(1)
