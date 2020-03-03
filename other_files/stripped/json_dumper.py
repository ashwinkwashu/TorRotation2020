import pickle
import json

counts_v2, counts_v3, filenames, v2_desc_count, v3_desc_count  = pickle.load(open("arraydump.pkl",'rb'))

print(len(counts_v2[0]), len(counts_v3[0]), len(filenames))

a1 = []
b1 = []
for i in range(len(filenames)):
	a={}
	b={}
	a['time'] = filenames[i][:-10].replace('+',' ')
	a['data'] = [{"x":filenames[j][:-10].replace('+',' ') ,"y":counts_v2[i][j][0]} for j in range(len(counts_v2[i]))]
	a['counts'] = v2_desc_count[i]
	a1.append(a)
	b['time'] = filenames[i][:-10].replace('+',' ')
	b['data'] = [{"x":filenames[j][:-10].replace('+',' ') ,'y':counts_v3[i][j][0]} for j in range(len(counts_v3[i]))]
	b['counts'] = v3_desc_count[i]
	b1.append(b)


c1 = []
d1 = []



for i in range(len(filenames)):
	
	c= {}
	d = {}
	c['time'] = filenames[i][:-10].replace('+',' ')
	c['data'] = [{"x":filenames[j][:-10].replace('+',' ') ,'y':counts_v2[i][j][1]} for j in range(len(counts_v2[i]))]
	c['counts'] = v2_desc_count[i]
	c1.append(c)
	d['time'] = filenames[i][:-10].replace('+',' ')
	d['data'] = [{"x":filenames[j][:-10].replace('+',' ') ,'y':counts_v3[i][j][1]} for j in range(len(counts_v3[i]))]
	d['counts'] = v3_desc_count[i]
	d1.append(d)

e1 = []
f1 = []



for i in range(len(filenames)):
	
	e= {}
	f = {}
	e['time'] = filenames[i][:-10].replace('+',' ')
	e['data'] = [{"x":filenames[j][:-10].replace('+',' ') ,'y':counts_v2[i][j][0] - counts_v2[i][j][1]} for j in range(len(counts_v2[i]))]
	e['counts'] = v2_desc_count[i]
	e1.append(e)
	f['time'] = filenames[i][:-10].replace('+',' ')
	f['data'] = [{"x":filenames[j][:-10].replace('+',' ') ,'y':counts_v3[i][j][0] - counts_v3[i][j][1]} for j in range(len(counts_v3[i]))]
	f['counts'] = v3_desc_count[i]
	f1.append(f)

# print(filenames, c1[30]["time"])

with open('v2_json_dump.json', 'w') as outfile:
    json.dump(a1[::-1], outfile)

with open('v3_json_dump.json', 'w') as outfile:
    json.dump(b1[::-1], outfile)

with open('v2_replicas_json_dump.json', 'w') as outfile:
    json.dump(c1[::-1], outfile)

with open('v3_replicas_json_dump.json', 'w') as outfile:
    json.dump(d1[::-1], outfile)

with open('v2_uniques_json_dump.json', 'w') as outfile:
    json.dump(e1[::-1], outfile)

with open('v3_uniques_json_dump.json', 'w') as outfile:
    json.dump(f1[::-1], outfile)
# import pygame

# def printer(screen,name,val,pos):
#     tbox=font.render(name+' = '+str(val),True,(20,25,25))
#     screen.blit(tbox,pos)




#for each time, process the time, on a horizontal axis show time, vertical axis show replicas/
