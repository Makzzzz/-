a='+a+b+k+f+s+'
b=[]
c=0
d=1
for i in range (len(a)):
    if a[i]!='+':
        if a[i-1]=='+' and a[i+1]=='+':
            b.append(c)
        else:
            b.append(d)
s=sum(b)
if s==0:
    print('true')
else: 
    print('false')