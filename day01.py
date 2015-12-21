a = float(raw_input("Enter 1st no.: "))
b = float(raw_input("Enter 2nd no.: "))
c = input("Enter 3rd no.: ")
d = input("Enter 4th no.: ")
add = a + b
sub = a - b
mul = a*b
div = a/b
print "values are "
print "a = ", a
print "b = ", b
print "c = ", c
print "d = ", d

if a==1:
	print "addition =", add
elif a==3:	
	print "substraction =", sub
	if b==5:
		print "division =", div
	else:
		print "multiplication =", mul
else:
	print "nothing"

print c + d
l2 = [add ,sub, div,mul]
l1 = [a,b,c,d]
print "l1[0] = ", l1[0]
print "l1[1] = ", l1[1]
print "l1[2] = ", l1[2]
print "l1[3] = ", l1[3]

print l1
print l2
	


