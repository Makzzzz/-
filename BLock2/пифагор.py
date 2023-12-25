import math
ax=1
bx=1
ay=1
by=2
def pifagor(ax,bx,ay,by):
    n=math.sqrt(((bx-ax)**2)+((by-ay)**2))
    n=round(n,0)
    print(n)
pifagor(ax,bx,ay,by)