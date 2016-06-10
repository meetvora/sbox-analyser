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

###		FUNCTIONS		###
def QSterms(anf):
	TERMS =[]
	for i in range(4):
		term = []
		for index in xrange(len(anf[i])):
			if anf[i][index] == '1':
				temp = ('{0:0' + str(IN + LEADERS) + 'b}').format(index)[::-1]
				temp_str = ''
				for j in xrange(len(temp)):
					if temp[j] == '1':
						temp_str += chrs[j] 
				if int(temp) == 0:
					temp_str = '0'
				term.append(temp_str)
				term.sort()
		TERMS.append(term)
	return TERMS

def QSBox(p, q, l):
	x, y = p, q
	c = 0
	for i in l:
		if c%2 == 0:
			x = S[4*i + x]
			y = S[4*x + y]
		else:
			y = S[4*i + y]
			x = S[4*y + x]
		c += 1
	return x, y

def QSfunction(S):
	L = list(itertools.permutations(range(4)))
	F = {}
	for j in range(16):
		p ,q =  j/4, j%4
		str_n = ('{0:0' + str(4) + 'b}').format(j)
		for k in range(256):
			f = ('{0:0' + str(8) + 'b}').format(k)
			l = [f[m:m+2] for m in range(0, 8, 2)]
			l = [int(m,2) for m in l]
			x, y = QSBox(p, q, l)
			F[f+str_n] = ('{0:0' + str(2) + 'b}').format(x) + ('{0:0' + str(2) + 'b}').format(y)
	return F

def QSEquation(T):
	final_out = ""
	for i, t in enumerate(T):
		out = '\nFor Y' + str(OUT-i)+':\n'
		for e in t:
			if len(e)>1:
				vmap = [var_map[c] for c in e]
				vmap = '*'.join(vmap)
			else:
				vmap = var_map[e]
			out += vmap +" + "
		final_out += (out[:-2])
	return final_out

def QSdegree(anf):
	D = []
	for i in xrange(OUT):
		d = 0
		for j in xrange(len(anf[i])):
			if anf[i][j]=='1':
				if weight(bin(j)[-IN:]) > d:
					d = weight(bin(j))
		D.append(d)
	return D

###		MAIN		###
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

