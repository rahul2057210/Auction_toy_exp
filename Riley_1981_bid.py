import pandas as pd
import numpy as np  
import scipy
import matplotlib.pyplot as plt 

from scipy.misc import logsumexp

np.random.seed(0)

N = 2
P = []
for j in range(40000):

	v1 = np.random.uniform(0,1,1)

	v2 = np.random.uniform(0,1,1)

	c = (N-1.0)/(N)
	b1 = c*v1
	b2 = c*v2

	P.append(max(b1,b2))

#print(np.mean(P),np.var(P))

mean_true = (N-1)/(N+1)
var_true = ( (N-1)**2 )/( N* ( (N+1)**2) * (N+2)  ) 

#print(mean_true,var_true)


### Sad loser auction: there is entry fee c such that only people above V* enter

c=1.0/4

N = 2
P = []
nu_star = 1.0/2

for j in range(60000):
	val = 0
	b1 = 0
	b2 = 0 
	v1 = np.random.uniform(0,1,1)

	v2 = np.random.uniform(0,1,1)

	if v1>nu_star:
		val = val + c + 0.0
		b1 = (v1**2 - 0.25)/( 2*(1-v1) )
	if v2>nu_star:
		val = val + c + 0.0
		b2 = (v2**2 - 0.25)/( 2*(1-v2) ) 

	val = val + min(b1,b2)
	P.append(val)

print(np.mean(P),np.var(P))


### Second bid auction with buyer reservation value V*

N = 2
P = []
nu_star = 1.0/2

for j in range(60000):
	val = 0 
	b1 = 0
	b2 = 0
	v1 = np.random.uniform(0,1,1)

	v2 = np.random.uniform(0,1,1)

	if v1>nu_star:
		b1 = v1 + 0.0
	if v2>nu_star:
		b2 = v2 + 0.0

	if b1>0 or b2>0:
		P.append(max(nu_star,min(b1,b2)) )
	else:
		P.append(min(b1,b2))

print(np.mean(P),np.var(P))

###  Santa Claus auction with buyer reservation value V*

N = 2
P = []
nu_star = 1.0/2

for j in range(60000):
	val = 0 
	b1 = 0
	b2 = 0
	v1 = np.random.uniform(0,1,1)

	v2 = np.random.uniform(0,1,1)

	if v1>nu_star:
		b1 = v1 + 0.0
		val = val + 0.5*( (v1**2)-(nu_star**2) )
	if v2>nu_star:
		b2 = v2 + 0.0
		val = val + 0.5*( (v2**2)-(nu_star**2) )


	if b1>0 or b2>0:
		P.append(max(b1,b2)-val ) 
	else:
		P.append(0)

print(np.mean(P),np.var(P))






