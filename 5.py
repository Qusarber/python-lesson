ms = [-1,7,2,3,1,6]
k=0
ms.sort()
for i in range(len(ms)-1):
	if k > ms[i]:
		if k in ms:
			k+=1
		elif k>0:
			break
	else:
		k+=1

print('Найбільше додатнє поза масивом', k)


	