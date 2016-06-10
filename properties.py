import math

IN, OUT = None, None
# FOR DES
# IN => 	Y6	Y5	Y4	Y3	Y2	Y1
# OUT =>	X4	X3	X2	X1

def set_length(In, Out):
	global IN
	global OUT
	IN, OUT = In, Out

def function_des(rows):
	f = {}
	for i, row in enumerate(rows):
		endbits = '{0:02b}'.format(i)
		k = endbits[0]
		for j, element in enumerate(row):
			value = ('{0:0' + str(OUT) + 'b}').format(int(element))
			key = k + ('{0:0' + str(OUT) + 'b}').format(j) + endbits[1]
			f[key] = value
	return f

def function_QS(S):
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

def truthtable_bitwise(f):
	tt = []
	for i in xrange(OUT):
		X = {}
		tti = ""
		for key, value in f.iteritems():
			X[key] = int(value[i])
		for k in sorted(X):
			tti += str(X[k])
		tt.append(tti)
	return tt

def sequence(tt):
	ff=[]
	for i in xrange(OUT):
		FF = []
		for c in tt[i]:
			FF.append(1 - 2*int(c))
		ff.append(FF)
	return ff

def algebraicform(tt):
	anf = []
	for m in xrange(OUT):
		anfi = [0] * (2**IN)
		for i in xrange(2**IN):
			for j in xrange(i+1):
				if j | i == i:
					anfi[i] = anfi[i] ^ int(tt[m][j])
		anf.append(''.join([str(s) for s in anfi]))
	return anf

def terms(anf):
	TERMS =[]
	for i in xrange(OUT):
		term = []
		for index in xrange(len(anf[i])):
			if anf[i][index] == '1':
				temp = ('{0:0' + str(IN) + 'b}').format(index)[::-1]
				temp_str = ''
				for j in xrange(len(temp)):
					if temp[j] == '1':
						temp_str += str(j+1)
				if int(temp) == 0:
					temp_str = '0'
				term.append(int(temp_str))
				term.sort()
		TERMS.append(term)
	return TERMS

def weight(x):
	if type(x) is str:
		return x.count('1')
	if type(x) is int:
		c=0
		if x!=0:
			l = int(math.log(x)/math.log(2))
			while(x):
				x = x & (x-1)
				c += 1
		return c

def mult(a, b):
	s = 0
	for i in xrange(len(a)):
		s += a[i]*b[i]
	return s

def walsh_hamadard_transform(seq):
	WHC, n = [], len(seq[0])
	for k in xrange(OUT):
		whc=[]
		for i in xrange(n):
			h=[]
			for j in xrange(n):
				h.append((-1)**weight(i&j))
			whci = mult(seq[k], h)
			whc.append(whci)
		WHC.append(whc)
	return WHC

def non_linearity(wht_list):
	NL, n =[], IN
	for i in xrange(OUT):
		NL.append(2**(n-1) - max(abs(wh) for wh in wht_list[i])/2)
	return NL

def degree(anf):
	D = []
	for i in xrange(OUT):
		d = 0
		for j in xrange(len(anf[i])):
			if anf[i][j]=='1':
				if weight(bin(j)) > d:
					d = weight(bin(j))
		D.append(d)
	return D

def all_prop(values):
	rows = [ values[17:33], values[34:50], values[51:67], values[68:84] ]
	f = function_generate(rows)
	tt = truthtable_bitwise(f)
	ff = sequence(tt)
	anf = algebraicform(tt)
	term = terms(anf)
	wht = walsh_hamadard_transform(ff)
	nl = non_linearity(wht)
	d = degree(anf)
	print f
	result = []
	for i in xrange(OUT):
		res =  '\nFOR X' + str(i+1) + '\nTT: \n' + tt[i] + '\nSEQUENCE:\n '+ ' '.join([str(f) for f in ff[i]]) + '\nANF: \n' + anf[i] + '\nWHT: \n' + ', '.join([str(wh) for wh in wht[i]]) + '\nNL: ' + str(nl[i]) + '\nWEIGHT: ' + str(weight(tt[i])) + '\nDEGREE: ' + str(d[i]) + '\nTERMS: ' + str(len(term[i])) + '\nBALANCE: ' + str(weight(tt[i]) == 2**(IN - 1)) + '\n'
		for t in term[i]:
			res += str(t) + ' '
		res += '\n'
		result.append(res)

	return result

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


