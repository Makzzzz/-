def shourtner(st):
    while '('in st or')' in st:
        left = st.rfind('(')
        right = st.rfind(')', left)
        st = st.replace(st[left:right + 1], '')
        return st
print(shourtner('Бамбимабамбум (5252525) ггвп ланая'))