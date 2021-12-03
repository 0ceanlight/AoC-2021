fp = open('1-1.txt', 'r')
last_pos = fp.tell()
line = fp.readline()

lc = 0
c = 0
sum = 0

while line != '':
	sum += int(line)
	if c == 0:
		last_pos = fp.tell()
	if c == 2:
		fp.seek(last_pos)	
		print(sum)
		sum = 0
		c = -1

	line = fp.readline()
	lc += 1
	c += 1

# result of this can be piped to the script for part 1 to count number of increases
# yes this is messy but at least I learned about tell and seek ;)
