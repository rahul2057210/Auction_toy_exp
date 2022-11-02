import pandas as pd
import numpy as np  
import scipy
import matplotlib.pyplot as plt 

from scipy.misc import logsumexp

np.random.seed(0)

N = 2

Payoff = []


#### Seller's revenue
for k in range(10):
	
	v1 = np.random.uniform(0,1,1)
	  
	
	# Case 1 : b1 = b1-0.01
	b1 = ( (2.0*v1)/3.0 ) + 0.25
	b1 = b1 - 0.1
	R_seller = []
	R_buyer = []
	for j in range(90000):
		

		v2 = np.random.uniform(0,1,1)

		
		#b1 = b1 - 0.01 
		b2 = ( (2.0*v2)/3.0 ) + (1.0/12) 
		if b1<=b2:

			R_seller.append((0.5*(b1+b2))-v1)

			R_buyer.append((-0.5*(b1+b2))+v2 )

		else:
			R_seller.append(0)

			R_buyer.append(0)


	print('seller_payoff',k,np.mean(R_seller))


	# Case 2 : b1 = b1+0.01
	b1 = ( (2.0*v1)/3.0 ) + 0.25
	b1 = b1 + 0.1
	R_seller = []
	R_buyer = []
	for j in range(90000):
		

		v2 = np.random.uniform(0,1,1)

		
		#b1 = b1 - 0.01 
		b2 = ( (2.0*v2)/3.0 ) + (1.0/12) 
		if b1<=b2:

			R_seller.append((0.5*(b1+b2))-v1)

			R_buyer.append((-0.5*(b1+b2))+v2 )

		else:
			R_seller.append(0)

			R_buyer.append(0)


	print('seller_payoff',k,np.mean(R_seller))

	# Case 2 : b1 = b1
	b1 = ( (2.0*v1)/3.0 ) + 0.25
	R_seller = []
	R_buyer = []
	for j in range(90000):
		

		v2 = np.random.uniform(0,1,1)

		
		#b1 = b1 - 0.01 
		b2 = ( (2.0*v2)/3.0 ) + (1.0/12) 
		if b1<=b2:

			R_seller.append((0.5*(b1+b2))-v1)

			R_buyer.append((-0.5*(b1+b2))+v2 )

		else:
			R_seller.append(0)

			R_buyer.append(0)


	print('seller_payoff',k,np.mean(R_seller))

	




#### Buyer's revenue
for k in range(10):
	
	v2 = np.random.uniform(0,1,1)
	  
	
	# Case 1 : b2 = b2 - 0.01
	b2 = ( (2.0*v2)/3.0 ) + (1.0/12)
	b2 = b2 - 0.1
	R_seller = []
	R_buyer = []
	for j in range(90000):
		

		v1 = np.random.uniform(0,1,1)

		b1 = ( (2.0*v1)/3.0 ) + 0.25
		#b1 = b1 - 0.01 
		 
		if b1<=b2:

			R_seller.append((0.5*(b1+b2))-v1)

			R_buyer.append((-0.5*(b1+b2))+v2 )

		else:
			R_seller.append(0)

			R_buyer.append(0)


	print('buyer_payoff',k,np.mean(R_buyer))


	# Case 2 : b2 = b2 + 0.01
	b2 = ( (2.0*v2)/3.0 ) + (1.0/12)
	b2 = b2 + 0.1
	R_seller = []
	R_buyer = []
	for j in range(90000):
		

		v1 = np.random.uniform(0,1,1)

		b1 = ( (2.0*v1)/3.0 ) + 0.25
		#b1 = b1 - 0.01 
		 
		if b1<=b2:

			R_seller.append((0.5*(b1+b2))-v1)

			R_buyer.append((-0.5*(b1+b2))+v2 )

		else:
			R_seller.append(0)

			R_buyer.append(0)


	print('buyer_payoff',k,np.mean(R_buyer))

	# Case 3 : b2 = b2 
	b2 = ( (2.0*v2)/3.0 ) + (1.0/12)
	R_seller = []
	R_buyer = []
	for j in range(90000):
		

		v1 = np.random.uniform(0,1,1)

		b1 = ( (2.0*v1)/3.0 ) + 0.25
		#b1 = b1 - 0.01 
		 
		if b1<=b2:

			R_seller.append((0.5*(b1+b2))-v1)

			R_buyer.append((-0.5*(b1+b2))+v2 )

		else:
			R_seller.append(0)

			R_buyer.append(0)


	print('buyer_payoff',k,np.mean(R_buyer))
