import re

str = ""
with open("log-799931.txt") as f:
    for s in f:
        str += s
str = str.replace(':null', ':"null"')
pat = "var message = (\[[^\]]+\])"
pat2 = re.compile(pat, re.MULTILINE)
ret = pat2.search(str)
print(ret)
if ret:
    str2 = ret.group(1)
    b = eval(str2)
    n = len(b)
    for i in range(n):
        print(i, b[i]["from_user"], "->", b[i]
              ["to_user"], b[i]["job"], b[i]["message"])
