from collections import defaultdict
n, m=map(int, input().split())
d = defaultdict(list)
for i in range(1, n+1):
    A=input()
    d[A].append(i)
for k in range(m):
    B=input()
    if B in d:
        for l in d[B]:
            print(l, end=" ")
        print()
    else:
        print(-1)
