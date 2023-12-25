a='Dokonca gang kruti'
def pudge(a):
    while 'o' in a:
        a=a.replace('o','0')
    while 'g' in a:
        a=a.replace('g','9')
    print(a)
pudge(a)