import re
def slozhnost(password):
    score = 0
    if len(password) >= 8:
        score += 1
    if re.search("[A-Z]", password):
        score += 1
    if re.search("[a-z]", password):
        score += 1
    if re.search("[0-9]", password):
        score += 1
    if re.search("[!@#$%^&*()-_+=]", password):
        score += 1
    return score
password = "hdcfxvhA!dd0"
print(slozhnost(password))