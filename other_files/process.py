#f = open('55fa1820b000-55fa320cd000.dump','r', encoding = "ISO-8859-1").read()
#g = f.split('rendezvous')
#print('v2: ',len(g)-1)
#h = f.split('hs-desc')
#print('v3: ',len(h)-1)
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
#print(g2[0])
#print('\n\n\n\n')

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
#print(h2[0])
print(len(h2))

