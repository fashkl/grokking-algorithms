
s = "22$$3"
ts = list(s)
comp = list(set(list(filter(lambda k: k != "$", s))))
se = set()
for i in comp:
    for index, j in enumerate(s):
        if j == "$":
            s[index] = str(i)
            print(s)
    se.add(''.join([str(elem) for elem in s]))
    s = ts

print(se)
