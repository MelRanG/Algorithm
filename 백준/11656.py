n = input()
s = []
for i in range(len(n)):
    s.append(n[i:])
for i in sorted(s):
    print(i)
    