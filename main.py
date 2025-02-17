from SNParameterEstimator import ParameterEstimator

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import skewnorm

# Define the number of samples, the location, the scale, and the skewness
num_samples = 10000
mu_data = 0.0  # location (mean) 
sd_data = 3.0  # scale (standard deviation) 
alpha_data = 5.0  # skewness (negative value means left skew, positive means right skew)

# Generate samples from the skew normal distribution
dist = skewnorm(alpha_data, mu_data, sd_data)
samples = dist.rvs(num_samples)
plt.hist(samples, bins=30, density=True, alpha=0.6, color='g')
xmin, xmax = plt.xlim()
# xmin = xmin + 2/12 * (xmax - xmin)
x = np.linspace(xmin, xmax, 1000)
p = skewnorm.pdf(x, alpha_data, mu_data, sd_data)
plt.plot(x, p, 'k', linewidth=2)
x_values = x 
y_values = p
plt.show()

# Computer the parameters using the function
mu, sd, alpha = ParameterEstimator(x_values, y_values, epochs=501, learning_rate=0.005, decay=1e-3, epsilon=1e-7, beta_1=0.9, beta_2=0.999)

print("Estimated location (mean): ", mu)
print("Estimated scale (standard deviation): ", sd)
print("Estimated skewness: ", alpha)