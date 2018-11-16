def normalize(name):
    return name[0].upper()+name[1:].lower()


L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


def format_name(s):
    return s.capitalize()
    # return s[0].upper() + s[1:].lower()


L3 = ['adam', 'LISA', 'barT']
L4 = list(map(format_name, L3))
print(L4)
