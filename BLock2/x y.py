a=[228,1337,312]
b=[52,63,17]
c=[]
def klikklak(a,b,c):
    for i in range (len(a)):
        h = a[i]
        k = b[i]
        g = str(h)+';'+str(k)
        c.append(g)
    print(c) 
klikklak(a,b,c)   