a = 23
b = 23
from time import time
def gcd(a,b):
    lst = []
    for i in range(1,a+1):
        if a %i ==0:
            if i not in lst:
                lst.append(i)
    for i in range(1,b+1):
        if b%i == 0:
            if i not in lst:
                lst.append(i)
    lst_finaal = []
    for i in range(len(lst)):
        if a % lst[i] == 0 and b % lst[i] == 0:
            lst_finaal.append(lst[i])
    return lst_finaal[len(lst_finaal)-1]
_start = time()
print(gcd(23,23))
_end = _start - time()
print(_end)