import os
z=""
lines = [line.rstrip('\n') for line in open('processes.txt')]
w=[]
for l in lines:
	w.append(int(l))
	#print int(l)
q=max(w)
for a in lines:
	if(q != int(a)):
		z+=str(a)+" "
e="kill -9 "+z
os.system(e)

		
	
	
