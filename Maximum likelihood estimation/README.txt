
This Python code (Maximum likelihood estimation.py) provides diffusion coefficient estimation using the two-dimensional trajectory of Brownian particles like single fluorescent molecules observed under TIRF microscope. Since the estimation is based on the statistical distribution of the displacement rather than the mean square displacement, individual diffusion coefficients can be estimated even if the trajectory is non-uniform. Based on the Akaike Information Criterion (AIC), it indicates the number of diffusion states with the highest probability of differing diffusion coefficients. In this code, maximum likelihood estimation is performed by a one-state model or a two-state model using the EM algorithm for the matrix of the diffusion displacement per unit time of a molecule. Expected run time for demo using “Data.csv” on a normal desktop computer is about 1 min. In the example of the output (Out_put.jpg)  shows the result of 1-state model, 2-state model and the convergence of the likelihood, respectively. For details, refer to the following article.

Matsuoka, S., Shibata, T. & Ueda, M. Statistical analysis of lateral diffusion and multistate kinetics in single-molecule imaging. Biophys J. 97, 1115-1124 (2009).

Matsuoka, S., Shibata, T. & Ueda, M. Asymmetric PTEN distribution regulated by spatial heterogeneity in membrane-binding state transitions. PLoS Comput Biol. 9, e1002862 (2013).

We has been tested on the following software.

Python 2.7.5 
IPython 2.0.0


1. Open Ipython.

2. Move to folder (Maximum likelihood estimation).

3. Copy and paste Python code (Maximum likelihood estimation.py).
When pasting code, we recommend using magic command “%paste”.

To adjust the initial value of the parameter, change the values of lines 46 and 47.
