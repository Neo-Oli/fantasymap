with open ("map.txt", "r") as myfile:
	data=myfile.read()
clist=list(data)
lastc=""
for c in clist:
	if c=="\"":
		pass
	elif c==",":
		pass
	elif c=="+":
		print(" m", end="")
	elif c=="X":
		print(" a", end="")
	elif c==lastc:
		print("  ", end="")
	else:
		if c==" ":
			print("w ", end="")
		elif c==".":
			print("g ", end="")
		elif c=="O":
			print("d ", end="")
		elif c=="o":
			print("i ", end="")
		else:
			print(c, end="")
	lastc=c
