a='1564, 45542, 6664, 7775'
b=1
c=[]
def multiple(a,b):
   for i in range(len(a)):
       if a[i]!=" " and a[i]!=",":
           n=int(a[i])
           c.append(n)      
   print(b)   
   for i in c:
       b=b*i
   print(b)
multiple(a,b)