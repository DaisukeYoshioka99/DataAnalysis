import numpy as np
import matplotlib.pyplot as pp
import sys

def gaussian(D,t): # Probability density function
	def f(x):
    		return x/(2*D*t+2* 0.00979236**2)*np.exp(-(x**2)/(4*D*t+4* 0.00979236**2)) #For the measurement error ε, the value calculated by MSD analysis was used.
	return f

def estimate_posterior_likelihood(X, pi, gf): # Calculation of posterior probability γ
    l = np.zeros((X.size, pi.size))
    for (i, x) in enumerate(X):
        l[i, :] = gf(x)
    return pi * l * np.vectorize(lambda y: 1 / y)((pi*l).sum(axis = 1).reshape(-1, 1))

def estimate_gmm_parameter(X, t, gamma):# Calculate parameters using γ
    N = gamma.sum(axis = 0)
    mu =( ((np.sum(gamma * (X**2).reshape((-1, 1)),0)/(4*N)))-0.00979236**2)/t # For the measurement error ε, the value calculated by MSD analysis was used.
    pi = N / X.size
    return (mu, pi)

def calc_Q(X, pi,gf):# Calculate likelihood 
	l = np.zeros(X.size)
	for (i, x) in enumerate(X):
		l[i] = pi[0]*gf(x)[0]+pi[1]*gf(x)[1]
	return np.sum(np.log(l))


def EM(X,t,gaussian,estimate_posterior_likelihood,estimate_gmm_parameter,calc_Q):
	## Number of data ##
	N = len(X)
	
	##### 1 state model #####
	D =( ((np.sum( (X**2).reshape((-1, 1)),0)/(4*N)))-0.00979236**2)/t #For the measurement error ε, the value calculated by MSD analysis was used.
	l = np.zeros(X.size)
	for (i, x) in enumerate(X):
		l[i] = gaussian(D,t)(x)		
	Q = np.sum(np.log(l))
	AIC1=-2*Q+2*(1+1) 
	
	##### 2 states model #####
	# termination condition
	K = 2
	epsilon = 0.01
	# initialize gmm parameter ##
	pi = np.array([0.3,0.7]) 
	mu = np.array([0.05,0.2])
	Q = -sys.float_info.max
	delta = None
	n=0
	Qn=np.zeros(10000)
	deltan=np.zeros(10000)
	# EM algorithm ##
	while delta == None or delta >= epsilon:
		gf = gaussian(mu, t)
		# E step: estimate posterior probability of hidden variable gamma
		gamma = estimate_posterior_likelihood(X, pi, gf)
		# M step: miximize Q function by estimating mu, sigma and pi
		mu, pi = estimate_gmm_parameter(X, t, gamma)
		# calculate Q function
		gf = gaussian(mu, t)
		Q_new = calc_Q(X, pi, gf)
		delta = abs(Q_new - Q)
		Q = Q_new
		Qn[n]=Q
		deltan[n]=delta
		n+=1		
	l = np.zeros(X.size)
	for (i, x) in enumerate(X):
		l[i] = pi[0]*gaussian(mu[0], t)(x)+pi[1]*gaussian(mu[1], t)(x)		
	Q = np.sum(np.log(l))
	AIC2=-2*Q+2*(2+1)

	return D, pi, mu, AIC1, AIC2, Qn, deltan


## Data reading ## 
disp=np.genfromtxt('Data.csv',delimiter=",",dtype='float64') ## Diffusion displacement of molecule per frame (μm)

## Maximum likelihood estimation ##
t=1.0/60 # Frame rate (msec)
Param=EM(disp,t,gaussian,estimate_posterior_likelihood,estimate_gmm_parameter,calc_Q)
	
## Figure ##
pp.figure(figsize=(15,5))
pp.subplots_adjust(wspace=0.4, hspace=0.2)

## Figure 1 (1 state model) ##
pp.subplot(1,3,1)
pp.hist(disp, bins=100,range=(0,1), normed = 1, alpha = 0.3)
seq = np.arange(0, 1, 0.01)
pp.plot(seq, gaussian(Param[0], t)(seq), linewidth = 2.0)
pp.xlim([0,0.5])
pp.title('D = '+str(np.around(Param[0],3))+', AIC = '+str(np.around(Param[3],3)))
pp.ylabel('Probability density')
pp.xlabel('Displacement ('+u'\u03bc'+'m)')

## Figure 2 (2 states model) ##
pp.subplot(1,3,2)
pp.hist(disp, bins=100,range=(0,1), normed = 1, alpha = 0.3)
seq = np.arange(0, 1, 0.01)
for i in range(2):
	pp.plot(seq, Param[1][i]*gaussian(Param[2][i],t)(seq), linewidth = 2.0)
	
pp.plot(seq, Param[1][0]*gaussian(Param[2][0],t)(seq)+Param[1][1]*gaussian(Param[2][1],t)(seq), linewidth = 2.0)
pp.xlim([0,0.5])
pp.title('D = '+str(np.around(Param[2],3))+', p = '+str(np.around(Param[1],3))+','+'\nAIC = '+str(np.around(Param[4],3)))
pp.ylabel('Probability density')
pp.xlabel('Displacement ('+u'\u03bc'+'m)')

## Figure 3 (Convergence of likelihood) ##
pp.subplot(1,3,3)
pp.plot(Param[5][Param[6]>0],'k-o',alpha = 0.8)
pp.xlim([0,len(Param[5][Param[6]>0])])
pp.ylabel('Likelihood')
pp.xlabel('Cycle')
pp.title('EM algorithm')
		
## Save image ##
pp.savefig('Displacement distribution.jpg')
pp.close()



















