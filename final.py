def max_missing_positive(lst1):
	rezlst = []
	k=1
	for i in range(max(lst1)):
		if k in lst1:
			k+=1
		elif k not in lst1 and k>0 and k<max(lst1):
			rezlst.append(k)
			k+=1
	if len(rezlst)==0:
		rezlst.append(max(lst1)+1)
	return max(rezlst)

assert max_missing_positive([1,2,4]) == 3
assert max_missing_positive([1,2,3,4,5]) == 6
assert max_missing_positive([1,2,4,5,6,8]) == 7