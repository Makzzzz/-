a=[1, 2, 3]
b=[4, 5, 6]
c=[7, 8, 9]
d=1
e=1
f=1
def korobka(a,b,c,d,e,f):
    for i in a:
        d=d*i
    for i in b:
        e=e*i
    for i in c:
        f=f*i
    v=d+e+f
    print(v)
korobka(a,b,c,d,e,f)