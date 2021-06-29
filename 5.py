ms = [1,2,3,4,5]
max = ms[0]
k=0

for i in range(len(ms)):
	if ms[i]>max:
		max = ms[i]
	if k<max:
		k += 1
	else:
		break

print('Мінімальне поза масивом', k+1)


	