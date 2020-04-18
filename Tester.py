a = []
with open('/Users/mkachimov/projects/Study/dataset_3380_5.txt', 'r') as b:
	for line in b:
		a.append(line.split())
d = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, '11': 0}
D = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, '11': 0}
for i in range(len(a)):
	d[a[i][0]] += int(a[i][2]) 
	D[a[i][0]] += 1
for i in d.keys():
	if d[i] == 0:
		d[i] = '-'
	else:
		d[i] /= D[i]
	print(i, d[i])