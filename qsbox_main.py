import itertools
from properties import *

#	Rounds = Leaders
#	input:	 L00 L0 L10 L11 L20 L21 L30 L31 (X4 X3 X2 X1)
#	output: Y4 Y3 Y2 Y1

####	GLOBAL DATA		###
IN = 4
LEADERS = 8 #Can be 8 or 4 only
OUT = 4
chrs = ['a','b','c','d','e','f','g','h','i','j','k','l']
var_map ={
	'0': '1', 
	'a':'X1', 'b':'X2', 'c':'X3', 'd':'X4', 'e':'L31', 'f':'L30', 'g':'L21', 'h':'L20', 'i':'L11', 'j':'L10', 'k':'L01', 'l':'L00'
}

#S  = [ 3, 2, 1, 0, 2, 0, 3, 1, 1, 3, 0, 2, 0, 1, 2, 3 ]
set_length(LEADERS + OUT, IN)
count = 1
box = open('qslist.txt', 'r').read().split('\n')
qsr = open('qsresult.txt', 'w')
for b in box:
	S = [int(u[-1])-1 for u in b.split()]	
	func = QSfunction(S)
	tt = truthtable_bitwise(func)
	anf = algebraicform(tt)
	D = QSdegree(anf)
	print count
	if D[0] == 3:
		print D
		print S
		T = QSterms(anf)
		final = QSEquation(T)
		qsr.write(str(count) +'\t\t\t['+ ' '.join([str(i) for i in D]) +']\n'+ final+ '\n\n\n')
	print count
	count += 1
qsr.close()

