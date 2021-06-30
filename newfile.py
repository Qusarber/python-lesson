ms = [-1,3,4,5,7,12,2,15]
ks = []
k=1
for i in range(max(ms)):
  if k in ms:
    k+=1
  elif k not in ms and k>0 and k<max(ms):
    ks.append(k)
    k+=1

if len(ks)==0:
	ks.append(max(ms)+1)
print('Перелік пропущених', ks)
print('Найбільше додатнє пропущене', max(ks))