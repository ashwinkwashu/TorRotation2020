files = ['55fa1820b000-55fa320cd000.dump',
'55fa1820b000-55fa327bd000.dump',
'55fa1820b000-55fa31f02000.dump',
'55fa1820b000-55fa327e1000.dump',
'55fa1820b000-55fa33056000.dump',
'55fa1820b000-55fa33298000.dump',
'55fa1820b000-55fa329de000.dump',
# '55fa1820b000-55fa32ef9000.dump',
'55fa1820b000-55fa32ef9000.dump',
'55fa1820b000-55fa3313a000.dump',
'55fa1820b000-55fa32e50000.dump',
'55fa1820b000-55fa318de000.dump',
'55fa1820b000-55fa32d38000.dump']

dim = len(files)

v2_list = [[] for i in range(dim)]
v3_list = [[] for i in range(dim)]
g_dims  = [ 0 for i in range(dim)]
h_dims  = [ 0 for i in range(dim)]
v2_descs = []
v3_descs = []

for ii in range(dim):
	print(files[ii])
	f = open(files[ii],'r', encoding = "ISO-8859-1").read()
	g = f.split('rendezvous-service-descriptor')
	g = g[1:]
	g2 = []
	for i in g:
		k = i.split('END SIGNATURE')
		k2 = k[1].split('\n')
		# print(k[0])
		g2+=['rendezvous-service-descriptor'+k[0]+'END SIGNATURE'+k2[0],]
	print('v2: ',len(g))
	g_dims[ii] = len(g)
	v2_descs.append(g2)
	# print(g2[0])
	# print('\n\n\n\n')

	h = f.split('hs-descriptor 3')
	h = h[1:]
	h2 = []
	for i in h:
		k = i.split('signature')
		if len(k)>1:
			k2 = k[1].split('\n')
		else:
			k2 = ['']
		h2.append('hs-descriptor 3'+k[0]+'signature'+k2[0])

	print('v3: ',len(h))
	h_dims[ii] = len(h)
	v3_descs.append(h2)
	# print(h2[0])
	# print(len(h2))

	v2_list[ii] = []     #CHECK LENGTH OF THIS COMPARED TO LENGTH OF H2
	for el in g2:
		k = el.split('-----BEGIN RSA PUBLIC KEY-----')
		k = k[1]
		k = k.split('-----END RSA PUBLIC KEY-----')
		k=k[0]
		v2_list[ii].append(k)

	v3_list[ii] = []
	for el in h2:
		# k = el.split('signature')
		# k = k[1]
		k = el.split('-----BEGIN ED25519 CERT-----')
		k = k[1]
		k = k.split('-----END ED25519 CERT-----')
		k = k[0]
		v3_list[ii].append(k)


import pickle

# pickle.dump([v2_list, v3_list, g_dims, h_dims], open("aggregated.pkl", "wb"))
pickle.dump([v2_descs, v3_descs, v2_list, v3_list, g_dims, h_dims], open("stripped_desc.pkl", "wb"))

exit()


counts_v2 = [[0 for i in range(dim)] for j in range(dim)]
for i in range(dim):
	for j in range(dim):
		for el in v2_list[i]:
			if el in v2_list[j]:
				counts_v2[i][j]+=1

counts_v3 = [[0 for i in range(dim)] for j in range(dim)]
for i in range(dim):
	for j in range(dim):
		for el in v3_list[i]:
			if el in v3_list[j]:
				counts_v3[i][j]+=1
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