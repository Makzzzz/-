def gg(subst, st):
    if subst.lower() in st.lower():
        return "Есть контакт!"
    else:
        return "Мимо!"
print(gg("Бам", "Бамбимбахмут"))