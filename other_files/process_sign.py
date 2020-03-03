import sys
if len(sys.argv)>1:
	name = str(sys.argv[1])
else :
	name = '55fa1820b000-55fa320cd000.dump'
f = open(name,'r', encoding = "ISO-8859-1").read()
g = f.split('rendezvous')
g = g[1:]
g2 = []
for i in g:
	k = i.split('END SIGNATURE')
	k2 = k[1].split('\n')
	# print(k[0])
	g2+=['rendezvous'+k[0]+'END SIGNATURE'+k2[0],]
print('v2: ',len(g))
# print(g2[0])
# print('\n\n\n\n')

h = f.split('hs-desc')
h = h[1:]
h2 = []
for i in h:
	k = i.split('signature')
	if len(k)>1:
		k2 = k[1].split('\n')
	else:
		k2 = ['']
	h2.append('hs-desc'+k[0]+'signature'+k2[0])

print('v3: ',len(h))
# print(h2[0])
# print(len(h2))

v2_signatures = []
for el in g2:
	k = el.split('-----BEGIN RSA PUBLIC KEY-----')
	k = k[1]
	k = k.split('-----END RSA PUBLIC KEY-----')
	k=k[0]
	v2_signatures.append(k)

v3_signatures = []
for el in h2:
	k = el.split('signature')
	k = k[1]
	# k = el.split('-----BEGIN ED25519 CERT-----')
	# k = k[1]
	# k = k.split('-----END ED25519 CERT-----')
	# k = k[0]
	v3_signatures.append(k)

"""
###################################################################################################
"""
###################################################################################################
"""
"""
###################################################################################################
"""
"""
###################################################################################################
"""
"""
###################################################################################################
"""
"""

if len(sys.argv)>2:
	name = str(sys.argv[2])
else :
	name = '55fa1820b000-55fa320cd000.dump'
f = open(name,'r', encoding = "ISO-8859-1").read()
g = f.split('rendezvous')
g = g[1:]
g2 = []
for i in g:
	k = i.split('END SIGNATURE')
	k2 = k[1].split('\n')
	# print(k[0])
	g2+=['rendezvous'+k[0]+'END SIGNATURE'+k2[0],]
print('v2: ',len(g))
# print(g2[0])
# print('\n\n\n\n')

h = f.split('hs-desc')
h = h[1:]
h2 = []
for i in h:
	k = i.split('signature')
	if len(k)>1:
		k2 = k[1].split('\n')
	else:
		k2 = ['']
	h2.append('hs-desc'+k[0]+'signature'+k2[0])

print('v3: ',len(h))
# print(h2[0])
# print(len(h2))

v2_signatures_2 = []
for el in g2:
	k = el.split('-----BEGIN RSA PUBLIC KEY-----')
	k = k[1]
	k = k.split('-----END RSA PUBLIC KEY-----')
	k = k[0]
	v2_signatures_2.append(k)

v3_signatures_2 = []
for el in h2:
	k = el.split('signature')
	k = k[1]
	# k = el.split('-----BEGIN ED25519 CERT-----')
	# k = k[1]
	# k = k.split('-----END ED25519 CERT-----')
	# k = k[0]
	v3_signatures_2.append(k)

print(v3_signatures[0], v3_signatures_2[0])

count_keep_v2 = 0
count_keep_v3 = 0
count_new_v2 = 0
count_new_v3 = 0

for el in v2_signatures:
	if el in v2_signatures_2:
		count_keep_v2+=1

for el in v3_signatures:
	if el in v3_signatures_2:
		count_keep_v3+=1

print(count_keep_v2 , count_keep_v3)