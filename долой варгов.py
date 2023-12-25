a=['бро','бро','бро','враг']
b=['враг']
c=[]
for i in range (len(a)):
    k= a[i]
    for y in range (len(b)):
        f=b[y]
        if k!=f:
            c.append(k)
print(c)
