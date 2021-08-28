def check(i,j,c):
    if c == '>':
        return i >j
    if c == '<':
        return i < j
    return True

print(check(1,6, "<"))