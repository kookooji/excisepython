from functools import reduce

def  normalize(name):
    return name[:1].upper() + name[1:].lower()
L1 = ['adma','LISA','barT']
L2 = list(map(normalize,L1))
print(L2)
def prod(L):
    def f(x,y):
        return x*y
    return reduce(f,L)
print('3 5 7 9 =',prod([3,5,7,9]))
def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(fn, map(char2num, s))
