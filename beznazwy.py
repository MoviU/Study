n, k = map(int, input().split())
if 1 <= n <= 10 and 0 <= k <= 10:
	def C_job(x, y):
		if y == 0:
			return 1
		elif y > x:
			return 0
		else:
			ans = C_job(x - 1, y) + C_job(x - 1, y - 1)
			return ans
	print(C_job(n, k))
else: 
	exit()