import math

IN, OUT = None, None
# FOR DES
# IN => 	Y6	Y5	Y4	Y3	Y2	Y1
# OUT =>	X4	X3	X2	X1

def set_length(In, Out):
	global IN
	global OUT
	IN, OUT = In, Out

def function_generate(rows):
	f = {}
	for i, row in enumerate(rows):
		endbits = '{0:02b}'.format(i)
		k = endbits[0]
		for j, element in enumerate(row):
			value = ('{0:0' + str(OUT) + 'b}').format(int(element))
			key = k + ('{0:0' + str(OUT) + 'b}').format(j) + endbits[1]
			f[key] = value
	return f

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

def truthtable_rowwise(rows):
	tt_row =[]
	for row in rows:
		ti=''
		for element in row:
			ti +=('{0:0' + str(OUT) + 'b}').format(int(element))
		tt_row.append(ti)
	return tt_row

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
	
	result = []
	for i in xrange(OUT):
		res =  '\nFOR X' + str(i+1) + '\nTT: \n' + tt[i] + '\nSEQUENCE:\n '+ ' '.join([str(f) for f in ff[i]]) + '\nANF: \n' + anf[i] + '\nWHT: \n' + ', '.join([str(wh) for wh in wht[i]]) + '\nNL: ' + str(nl[i]) + '\nWEIGHT: ' + str(weight(tt[i])) + '\nDEGREE: ' + str(d[i]) + '\nTERMS: ' + str(len(term[i])) + '\nBALANCE: ' + str(weight(tt[i]) == 2**(IN - 1)) + '\n'
		for t in term[i]:
			res += str(t) + ' '
		res += '\n'
		result.append(res)

	return result
