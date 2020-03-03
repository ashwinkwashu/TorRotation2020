files = ['55fa1820b000-55fa320cd000.dump',
'55fa1820b000-55fa327bd000.dump',
'55fa1820b000-55fa31f02000.dump',
'55fa1820b000-55fa327e1000.dump',
'55fa1820b000-55fa33056000.dump',
'55fa1820b000-55fa33298000.dump',
'55fa1820b000-55fa329de000.dump',
'55fa1820b000-55fa32ef9000.dump',
'55fa1820b000-55fa32ef9000.dump',
'55fa1820b000-55fa3313a000.dump',
'55fa1820b000-55fa32e50000.dump',
'55fa1820b000-55fa318de000.dump',
'55fa1820b000-55fa32d38000.dump']

dim = len(files)

import pickle

v2_list, v3_list, g_dims, h_dims = pickle.load(open("aggregated.pkl",'rb'))


counts_v2 = [[len(list(set(v2_list[i]).intersection(set(v2_list[j])))) for i in range(dim)] for j in range(dim)]
counts_v3 = [[len(list(set(v3_list[i]).intersection(set(v3_list[j])))) for i in range(dim)] for j in range(dim)]

# counts_v2 = [[sum(x == y for x in v2_list[i] for y in v2_list[j])  for i in range(dim)] for j in range(dim)]

# counts_v3 = [[sum(x == y for x in v3_list[i] for y in v3_list[j])  for i in range(dim)] for j in range(dim)]

print('-------------------------------------------------------------------------------')
print('V2')
print()
top = '\t'
for i in range(dim):
	top += str(g_dims[i]) + '\t'
print(top)

for i in range(dim):
	line = str(g_dims[i]) +'\t'
	for j in range(dim):
		line = line + str(counts_v2[i][j]) + '\t'
	print(line)

print('-------------------------------------------------------------------------------')
print('V3')
print()

top = '\t'
for i in range(dim):
	top += str(h_dims[i]) + '\t'
print(top)

for i in range(dim):
	line = str(h_dims[i]) +'\t'
	for j in range(dim):
		line = line + str(counts_v3[i][j]) + '\t'
	print(line)