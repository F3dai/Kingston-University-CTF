import random

banana = "\N{banana}"

print("Monkey want banana. How many banans?")

for i in range(1000):
	n = random.randrange(20)

	print(banana*n)

	try:
		answer = int(input())
	except:
		print("int only")
		exit()

	if answer != n:
		print("Monkey sad")
		exit()

print("Monkey happy. kucss{monk3y_c0uNt}")
