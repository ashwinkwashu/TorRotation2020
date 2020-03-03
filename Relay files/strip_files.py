import os
import pickle
import sys
filenames = [f for f in os.listdir('.') if (os.path.isfile(f) and f[-6:] == '.dump2' )]
# if len(sys.argv)==1:
# 	exit()
# filenames = [str(sys.argv[1])]

dim = len(filenames)

for ii in range(dim):
	print(filenames[ii])

	with open(filenames[ii],'r', encoding = "ISO-8859-1") as readfile:
		f = readfile.read()
		g = f.split('rendezvous-service-descriptor')
		g = g[1:]
		g2 = []
		for i in g:
			k = i.split('END SIGNATURE')
			k2 = k[1].split('\n')
			g2+=['rendezvous-service-descriptor'+k[0]+'END SIGNATURE'+k2[0],]
		print('v2: ',len(g))

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

		name = filenames[ii][:-1] + 'strip'
		pickle.dump([g2, h2], open(name, "wb"))
