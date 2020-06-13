import requests
f = requests.get('https://ru.wikipedia.org/wiki/Python').text
def rozdelitel(x):
	x = x.split('<code>')
	X = ''
	for i in x:
		if '<' in i:
			x.remove(i)
	for i in x:
		X += i
	return set(X.split('</code>'))
print(rozdelitel(f))

