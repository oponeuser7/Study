data = []

while True:
	try:
		data.append(input())
		#처리할 내용
		#...
	except EOFError:
		break

print(data)