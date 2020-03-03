import os
filenames = ['55fa1820b000-55fa320cd000.dump',
'55fa1820b000-55fa327bd000.dump',
'55fa1820b000-55fa31f02000.dump',
'55fa1820b000-55fa327e1000.dump',
'55fa1820b000-55fa33056000.dump',
'55fa1820b000-55fa33298000.dump',
'55fa1820b000-55fa329de000.dump',
'55fa1820b000-55fa32ef9000.dump',
# '55fa1820b000-55fa32ef9000.dump',
'55fa1820b000-55fa3313a000.dump',
'55fa1820b000-55fa32e50000.dump',
'55fa1820b000-55fa318de000.dump',
'55fa1820b000-55fa32d38000.dump']
filenames = [f for f in os.listdir('.') if (os.path.isfile(f) and f[-10:] == '.dumpstrip' )]
# print(filenames)
filenames.sort()
# print(filenames)

dim = len(filenames)

import pickle

# v2_descs, v3_descs, v2_list, v3_list, g_dims, h_dims = pickle.load(open("stripped_desc.pkl",'rb'))
v2_descs = []
v3_descs = []
for i in range(dim):
	name = filenames[i]
	v2, v3 = pickle.load(open(name, 'rb'))
	v2_descs.append(v2)
	v3_descs.append(v3)

v2_struct = ["rendezvous-service-descriptor", "version", "permanent-key" , "secret-id-part", "publication-time", "protocol-versions", "introduction-points", "signature"]
v3_struct = ["hs-descriptor", "descriptor-lifetime", "descriptor-signing-key-cert", "revision-counter", "superencrypted", "signature"]

files = []
for ii in range(dim):
	file = {'v2':[], 'v3': []}
	total_corrupt = [0,0]
	for desc in v2_descs[ii]:
		item ={}
		corrupt = 0
		for i in range(len(v2_struct)-1):
			t = desc.split(v2_struct[i])
			if len(t) ==1:
				# print('corrupted')
				corrupt += 1
				continue

			#This corruption wasnt happening earlier. Recheck files.
			# print(v2_struct[i])
			t = t[1]
			t = t.split(v2_struct[i+1])
			item[v2_struct[i]] = t[0]
		t = desc.split(v2_struct[-1])
		if len(t) == 1:
			corrupt += 1
			continue
		t = t[1]
		item[v2_struct[-1]] = t
		total_corrupt[0] += corrupt
		if corrupt == 0:
			file['v2'].append(item)
		else:
			# print(corrupt,' parts corrupted/not found in file ',ii , '. Skipping')
			continue

	# print(len(file['v2']))
	for desc in v3_descs[ii]:
		item ={}
		corrupt = 0
		for i in range(len(v3_struct)-1):
			t = desc.split(v3_struct[i])
			if len(t) ==1:
				# print('corrupted')
				corrupt += 1
				continue
			# print(v3_struct[i])
			t = t[1]
			t = t.split(v3_struct[i+1])
			item[v3_struct[i]] = t[0]
		t = desc.split(v3_struct[-1])
		t = t[1]
		item[v3_struct[-1]] = t
		if t=='':
			# print('corrupt')
			corrupt+=1
		total_corrupt[1] += corrupt
		if corrupt == 0:
			file['v3'].append(item)
		else:
			# print(corrupt,' parts corrupted/not found. Skipping')
			continue

	files.append(file)
	# print('--------------------------------------------------------------------------------------------------')
	# print('total corrupt', total_corrupt)
	# print('--------------------------------------------------------------------------------------------------')

# print(files[0]['v3'][0])

def compare_files(ind1,ind2, ver, flag = None):
	f1 = files[ind1][ver]
	f2 = files[ind2][ver]
	
	if flag:
		f1_flag = [i[flag] for i in f1]
		f2_flag = [i[flag] for i in f2]
		counts_flag = sum(x == y for x in f1_flag for y in f2_flag)
		# counts_flag = len(list(set(f1_flag).intersection(set(f2_flag))))
		return counts_flag
	counts = len(list(set(f1).intersection(set(f2)))) #can't hash dicts
	return counts

def check_common(ind1,ind2, ver, flag = None):
	f1 = files[ind1][ver]
	f2 = files[ind2][ver]
	
	if flag:
		f1_flag = [i[flag] for i in f1]
		f2_flag = [i[flag] for i in f2]
		print(list(set(f1_flag).intersection(set(f2_flag))))

def get_commons(ind1,ind2, ver, flag = None):
	#function to get a list of common descriptors across files using flag 
	if flag == None or 1:
		if ver=='v3':
			flag = "descriptor-signing-key-cert"
		else:
			flag = "permanent-key"

	f1 = files[ind1][ver]
	f2 = files[ind2][ver]
	common1 = []
	common2 = [] 
	replicas = 0
	for item1 in f1:
		for item2 in f2:

			if item2[flag] == item1[flag]:
				common1.append(item1)
				common2.append(item2)
				#This will add an item twice if there are items with duplicate descriptors
			if item1 == item2:
				replicas+=1


	replicas = count_replicas(common1, common2, ver)
	# print(common1[0], common2[0])
	# print(common1[0] == common2[0])
	# print((len(common1), replicas))
	return (len(common1), replicas)

def count_replicas(a1, a2, ver, flag = None):
	#given two lists from get_commons, check whether corresponding elemnts are entire duplicates or not, using flag
	if flag == None:
		if ver=='v3':
			flag = "signature"
		else:
			flag = "publication-time"
	count = 0
	if len(a1) != len(a2):
		raise ArraysShouldBeEqual
		exit()
	for i in range(len(a1)):
		if a1[i][flag] == a2[i][flag]:
			count+=1
	return count


# counts_v2 = [[len(list(set(files[i]['v2']).intersection(set(files[j]['v2'])))) for i in range(dim)] for j in range(dim)]
# counts_v3 = [[len(list(set(files[i]['v3']).intersection(set(files[j]['v3'])))) for i in range(dim)] for j in range(dim)]

# counts_v2 = [[compare_files(i,j,'v2', "permanent-key") for i in range(dim)] for j in range(dim)]
# counts_v3 = [[compare_files(i,j,'v3', "descriptor-signing-key-cert") for i in range(dim)] for j in range(dim)]   #DOESNT WORK> NOT A GOOD APPROACH AS IT USES SETS WHICH REMOVE ANY DUPLICATES (EG: Try lifetime)

counts_v2 = [[get_commons(i,j,'v2') for i in range(dim)] for j in range(dim)]
counts_v3 = [[get_commons(i,j,'v3') for i in range(dim)] for j in range(dim)]

v2_desc_count = [len(files[i]['v2']) for i in range(dim)]
v3_desc_count = [len(files[i]['v3']) for i in range(dim)]

pickle.dump([counts_v2, counts_v3, filenames, v2_desc_count, v3_desc_count], open('arraydump.pkl', "wb"))

# print('-------------------------------------------------------------------------------')
print('V2')
print()
top = '\t\t'
for i in range(dim):
	top += str(len(files[i]['v2'])) + '\t'
print(top)

for i in range(dim):
	line = filenames[i] +'\t'+str(len(files[i]['v2'])) +'\t'
	for j in range(dim):
		line = line + str(counts_v2[i][j]) + '\t'
	print(line)

# print('-------------------------------------------------------------------------------')
print('V3')
print()

top = '\t\t'
for i in range(dim):
	top += str(len(files[i]['v3'])) + '\t'
print(top)

for i in range(dim):
	line =filenames[i] +'\t' + str(len(files[i]['v3'])) + '\t'
	for j in range(dim):
		line = line + str(counts_v3[i][j]) + '\t'
	print(line)


# print(compare_files(3, 3, 'v3',"descriptor-lifetime"))
# get_commons(3,9,'v3',"descriptor-lifetime")
# counts_v2 = [[sum(x == y for x in v2_list[i] for y in v2_list[j])  for i in range(dim)] for j in range(dim)]




#ISSUE TO RESOLVE: V2 DOESNT SEEM TO DROP CORRUPTED DESCS. CHECK
#OK It drops one. BUT THERE SEEM TO BE MORE. THERE ARE DISCREPANCIES IN THE NUMBERS> FIGURE IT OUT. THERE SHOULDNT BE DUPLICATES FOR V2! V3 sorted after removing corrupted ones

#FIND A WAY TO COMPARE ENTIRE DESCRIPTORS> MAYBE STORING INDICES?


#structure:
"""
V2
"rendezvous-service-descriptor" descriptor-id   (time dependent)
"version" version number
"permanent-key" 
	'-----BEGIN RSA PUBLIC KEY-----'
	RSA Public Key here
	'-----END RSA PUBLIC KEY-----'
"secret-id-part" secret-id-part     (time dependent)
"publication-time" YYYY-MM-DD HH:MM:SS
"protocol-versions" version string
"introduction points"
	"-----BEGIN MESSAGE-----"
	message
	"-----END MESSAGE-----"
"signature"
	"-----BEGIN SIGNATURE-----"
	signature
	"-----END SIGNATURE-----"


V3
"hs-descriptor" version number
"descriptor-lifetime" lifetime in minutes
"descriptor-signing-key-cert"
	"-----BEGIN ED25519 CERT-----"
	cert
	"-----END ED25519 CERT-----"
"revision-counter" number
"superencrypted"
	"-----BEGIN MESSAGE-----"
	encrypted message
	"-----END MESSAGE-----"
"signature" signature
"""
