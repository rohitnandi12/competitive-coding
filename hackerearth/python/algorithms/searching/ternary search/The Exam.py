# https://www.hackerearth.com/practice/algorithms/searching/ternary-search/practice-problems/algorithm/the-exam/

# Write your code here
T = int(input())
while(T):
	x,l,n = map(int,input().split())
        
	if(n==0): # no need to go to any room
		print(0)
	elif(x==0): # twice of 0 is 0, hence unlimited access to room
		print(0)
	elif(l==0): # no other option, other than reducing X to zero
		print(x)
	elif(n==1): # To enter room only once
		if(x<=l): # no need to reduce
			print(0)
		else:
			print(x-l) # reduce x equal to l
	elif(n>55): # 2**56 will be greater than 10^18 hence reduce X to zero only solution
		print(x)
	else:
	    # Below is derived from the fact that
	    # L >= [r + 2*r + 4*r + .... + (2^n*r)]   NOTE: right hand side equation is sum of Geometric Progression
	    # what should be the value of r, so that irrespective of doubling it N times, it remains 
	    # less than L
	    # so x should be reduced to r, it means total mana used will be (x-r)
		d = x-(l//(2**(n-1)))
		if(d<=0):
			print(0)
		else:
			print(d)
			
	T -= 1