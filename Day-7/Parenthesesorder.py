def printParenthesis(str, pos, n,open, close):
	#print(str,pos,n,open,close)
	if(close == n):
		for i in str: 
			print(i, end="")
		print()
		return
	else:
		if(open > close):
			str[pos] = ')'
			printParenthesis(str, pos + 1, n,open, close + 1)
		if(open < n):
			str[pos] = '('
			printParenthesis(str, pos + 1, n,open + 1, close)


n = 1
str = [""] * 2 * n
printParenthesis(str, 0,n,0,0)