def foo(*args):
    a = []
    for x in args:
        a.append(x.upper())
    return sorted(a)


s1 = foo("rajini","sudhA","Aadhith")
s2 = foo("rajini","iniya")
print(s1, s2)
