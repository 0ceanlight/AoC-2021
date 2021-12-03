
counter = 0
lastline = 1000000000000000

f = open('1-2.txt','r')
for l in f:
	if int(l) > lastline: counter += 1
	lastline = int(l)

print(counter)
