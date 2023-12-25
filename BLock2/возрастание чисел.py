a=[1,2,3,4,5,6]
b=0
def funccia(a,b):
    for i in range(len(a)-1):
        if a[i]<a[i+1]:
            b=b+1
    if b>=(len(a)-1):
        print('возрастает')
    else:
        print('не возрастает')
funccia(a,b)