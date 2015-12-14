import sys, os, properties

print 'Make sure all look-up tables are placed correctly. \nEnter the number of'
print 'IN-bits: \t',
IN = int(raw_input())
print 'OUT-bits:\t',
OUT = int(raw_input())

properties.set_length(IN, OUT)
SB_COUNT = len(os.listdir('tables/'))

print 'There are ' + str(SB_COUNT) + ' files in tables. Enter \'N\' or \'n\' if incorrect, else press any other key to continue.'
ctr_valid = raw_input().lower()
if ctr_valid == 'n':
	print 'Rerun after checking files.'
	sys.exit()

for i in xrange(SB_COUNT):
	filename = "sbox_" + str(i+1) + ".txt"
	with open("tables/" + filename, 'r') as table:
		look_up = table.read()
	look_up = look_up.split()
	output = properties.all_prop(look_up)
	with open("results/" + filename, 'w') as result:
		for j in xrange(OUT):			
			result.write(output[j])

print 'Results stored successfully.\n'