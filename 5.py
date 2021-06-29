ms = [7,2,3,1,6]
k=0
ms.sort()
for i in range(len(ms)):
	if k > ms[i]:
		if k in ms:
			k+=1
		else:
			break
	else:
		k+=1

maxout = k-1
print('Найбільше додатнє поза масивом', maxout)


	