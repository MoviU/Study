a = [1, 3, 5, 7, 8]
c = []
b = 0; g = 0
for i in a:
	b += i
b /= len(a)
for i in a:
	c.append((i - b) ** 2)
for i in c:
	g += i
g = g / (len(a) - 1)
print(g ** 0.5)