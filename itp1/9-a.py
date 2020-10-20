w = input()
T = ""
ans = 0
e = True

while e:
    istr = input()
    if istr == "END_OF_TEXT":
        e = False
        break
    T = T + " " + istr

for i in T.split(" "):
    if i.lower()==w.lower():
        ans += 1
print(ans)
