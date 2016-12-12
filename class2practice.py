def mean(lst):
	m = float(0) 
	for i in range(0, len(lst)):
		m += lst[i]

	return m/len(lst)

print(mean([1,2,3]))

def median(lst):
	midIndex = len(lst)
	if ((len(lst)%2) ==0 ):
		return
	pass