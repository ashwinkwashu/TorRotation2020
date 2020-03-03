import sys
if len(sys.argv)>1:
	name = str(sys.argv[1])
else :
	name = '55fa1820b000-55fa320cd000.dump'
f = open(name,'r', encoding = "ISO-8859-1").read()
g = f.split('rendezvous')
g = g[1:]
print('v2: ',len(g))

h = f.split('hs-desc')
h = h[1:]
print('v3: ',len(h))
