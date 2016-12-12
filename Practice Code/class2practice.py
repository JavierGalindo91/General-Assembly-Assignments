'Javier Galindo'

def mean(lst):
	m = float(0) 
	for i in range(0, len(lst)):
		m += lst[i]

	return m/len(lst)

assert mean([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 4.5

def median(lst):
	lst.sort()
	if (len(lst)%2 ==0):
		midIndex = len(lst)/2
		median = (lst[midIndex] + lst[midIndex -1])/2.
		return median
	else:
		median = lst[len(lst)/2]
		return median


assert median([0, 1, 2, 5, 6, 8]) == 3.5
assert median([0, 3, 5, 8, 100]) == 5


def mode(lst):
    d = {}
    for item in lst:
    	d[item] = 0
    for x in lst:
    	if x in d.keys():
    		d[x] += 1

    a = []
    for (key, val) in sorted(d.items()):
    	if max(d.values())==1:
    		return None
    	else:
    		if val == max(d.values()):
    			a.append(key,)
    return a
   
assert mode([0, 1, 1, 1, 3, 6]) == [1, ]
assert mode([0, 1, 2, 2, 5, 5]) == [2, 5]
assert mode(range(100)) == None

def my_max(lst):
	lst.sort()
	return lst[-1]

assert my_max([0, 10, 39, 1000]) == 1000
assert my_max([0, 100, 100]) == 100

def my_min(lst):
	lst.sort()
	return lst[0]

assert my_min([0, 5, 10]) == 0
assert my_min([-1000, 1000, 0]) == -1000

def quartile(lst):
	index = len(lst)/4
	bigList =[]
	fq = lst[:index]
	sq = lst[index: index + 4]
	tq = lst[(index)*(-2): (index)*(-1)]
	ftq = lst[-index:]
	bigList.append(fq); bigList.append(sq); bigList.append(tq); bigList.append(ftq); 

	return bigList
assert quartile(range(16)) == [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]

def interquartile_range(lst):
    """ returns interquartile range """
    index = len(lst)/4
    return "range(%d,%d)"% (index, len(lst)- index)

#assert interquartile_range(range(16))

def variance(lst):
    """ returns variance """
    n = float(len(lst))
    variance = []

    for i in lst:
    	x = (mean(lst) - i)**2
    	variance.append(x)
    return sum(variance) / (n -1.0)

print variance([1,5,9,100])

def standard_deviation(lst):
	return variance(lst)**0.5
#assert standard_deviation([10,20,20,50]) == 15

def standard_error(lst):
    """ returns standard error """
    pass

def covariance(lst1, lst2):
	n = len(lst1) - 1
	covariance =0
	
	for x,y in zip(lst1, lst2):
		covariance += (x -mean(lst1))* (y - mean(lst2))
	return covariance / n

assert covariance([1,2,3], [4,5,9]) == 2.5