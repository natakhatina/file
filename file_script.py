import math,random
def fooCos(x):
    yield math.cos(x)
def fooSin(x):
    yield math.sin(x)


def foo(n):
    x=random.randint(0,180)
    x=x* math.pi/180
    for i in range(n):
        if x%2==0:
            a=fooSin(x)
            yield next(a)
        else:
            a=fooCos(x)
            yield next(a)


L=[x for x in foo(50)]
print(L)