b = [0, 0]
a = int(input())
for i in range(a):
	c = input().split()
	if c[0] == 'север' or c[0] == 'юг':
		b[1] += int(c[1])
	else:
		b[0] += int(c[1])
print(b)
