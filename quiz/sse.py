import math

def dist(x,y,m,n):
	ds = (x-m)*(x-m) +(y-n)*(y-n)
	return math.sqrt(ds)

def l2(x,y):
	print dist(x,y,0,0) > dist(x,y,100,40)

def l1(x,y):
	print ( abs(x - 0) + abs( y - 0) ) > (abs(x - 100) + abs( y - 40))

p = [(53,18),(63,8),(56,13),(52,13)]


for pi in p:
	print pi
	l1( pi[0],pi[1])
	l2( pi[0],pi[1])
