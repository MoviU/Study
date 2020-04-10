a = int(input())
s = set()
S = set()
for i in range(a):
	s.add(input().lower())
b = int(input())
for i in range(b):
	d = input().lower().split()
	for j in d:
		if j in s:
			continue
		else:
			S.add(j)
for i in S:
	print(i)

