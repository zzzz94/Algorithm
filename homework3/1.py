def is_palindrome(s):
	if len(s) == 1 or len(s) == 0:
		return True
	if s[0] == s[-1]:
		return is_palindrome(s[1:-1])
	else:
		return False


def min_count(s):
	for i in range(len(s) - 2, -1, -1):
		for j in range(i + 1, len(s)):
			if is_palindrome(s[i: j + 1]):
				count[i][j] = 0
			else:
				min = len(s)
				for k in range(i+1, j+1):
					if count[i][k-1] + count[k][j] + 1 < min:
						min = count[i][k-1] + count[k][j] + 1
				count[i][j] = min
	return count[0][len(s) - 1]


s = 'aabbaaba'
count =[[0 for _ in range(len(s))] for _ in range(len(s))]
print(min_count(s))