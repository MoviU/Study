zapis = int(input())
d = dict()
scopes = {'global': {'parent': None, 'variables': set()}}
def get(numsp, name):
	if numsp == 'global':
		if name in d[numsp]:
			return 'global'
		else:
			return 'None'
	try:
		g = 0
		if name in d[numsp]:
			return numsp
		elif name not in d[numsp]:
			for i in d.keys():
				if d.get(scope,None) is None:
        			return None
				if g == 0:
					if numsp in d[i] and name in d[i]:
						return i
					elif name in d[i]:
						return i
				if i == numsp:
					g += 1
	except TypeError:
		return 'None'
if 0 < zapis <= 100:
	for i in range(zapis):
		cmd, numsp, name = input().split()
		if cmd == 'create':
			if name in d.keys():
				d[name].append(numsp)
			else:
				d.setdefault(name, list())
				d.setdefault(numsp, list())
				d[name].append(numsp)
		elif cmd == 'add':
			if numsp not in d.keys():
				d.setdefault(numsp, list())
				d[numsp].append(name)
			elif numsp in d.keys():
				d[numsp].append(name)
		elif cmd == 'get':
			print(d)
			odp = get(numsp, name)
			print(odp)
print(d)