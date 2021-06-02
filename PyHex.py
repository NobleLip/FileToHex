import argparse

parser = argparse.ArgumentParser(description='File to HEX')
parser.add_argument('-f', dest='File', type=str,
                    help='Name of the File')

args = parser.parse_args()

f = open(args.File, 'r', encoding='latin1')
Buff = f.read()

Bytes = 0
Groups =0
for i in Buff:
	if Bytes % 16 == 0 and Bytes != 0:
		print('')
	if Groups % 2 == 0:
		print(' ', end= '')
		Groups = 0

	print(i.encode('latin1').hex() , end='')
	Bytes = Bytes + 1 
	Groups = Groups + 1
print('\n')
