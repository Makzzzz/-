def ne_ori(s: str):
    a = ''
    for b in s:
        a = b + a
    i = 0
    while a[i] == '?' or a[i] == '!':
        i += 1
    if i > 1:
        s = s[:len(s) + 1 - i]
    print(s)
    return s
print(ne_ori("привет!!!!"))