import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from lab2_funcs import *

fp = './Esperienza2.xlsx'
df = pd.read_excel(fp, skiprows = 1)

Gy = df['G_Y']
invGy = df['1/G_Y']
Delta_Gy = df['Delta_G_Y']
Delta_invGy = df['Delta_1/G_Y']
p_star = df['p*']
q_star = df['q*']
#Delta_p_star = df['Delta_p*']
Delta_q_star = df['Delta_q*']
Delta_p_star = 0.5

plt.errorbar(x = p_star, y = invGy, xerr = Delta_p_star, yerr = Delta_invGy, fmt = 'None')
plt.show()
plt.errorbar(x = q_star, y = Gy, xerr = Delta_q_star, yerr = Delta_Gy, fmt = 'None')
plt.show()
'''
plt.xlabel('$p^* [cm]$')
plt.setxlabel('$q^* [cm]$')
ax[0,0].setylabel('$G_Y$')
ax[0,0].setylabel('$1/G_Y$')
'''
#print(fit_lin(np.array([1,2,3]),np.array([2,4,6]),np.array([1,1,1])))

a1, b1, sigma_a1, sigma_b1, cov1, chi1 = fit_lin(p_star, invGy, 1/Delta_invGy**2)
a2, b2, sigma_a2, sigma_b2, cov2, chi2 = fit_lin(q_star, Gy, 1/Delta_Gy**2)

f1 = -1/a1
sigma_f1 = abs(sigma_a1/a1**2)
x1 = -(b1+1)/a1
sigma_x1 = np.sqrt(((b1+1)/a1**2)**2*sigma_a1**2 + a1**(-2)*sigma_b1**2 - 2*(b1+1)*cov1/a1**3)
f2 = 1/a2
sigma_f2 = abs(sigma_a2/a2**2)
x2 = -(b2+1)/a2
sigma_x2 = np.sqrt(((b2+1)/a2**2)**2*sigma_a2**2 + a2**(-2)*sigma_b2**2 - 2*(b2+1)*cov2/a2**3)

print('f1 = {:.2f} +/- {:.2f}'.format(f1, sigma_f1))
print('f2 = {:.2f} +/- {:.2f}'.format(f2, sigma_f2))
print('x1 = {:.2f} +/- {:.2f}'.format(x1, sigma_x1))
print('x2 = {:.2f} +/- {:.2f}'.format(x2, sigma_x2))
