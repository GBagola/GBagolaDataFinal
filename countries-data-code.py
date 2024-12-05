import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
from scipy.stats import kruskal
from scipy.stats import f_oneway
from scipy.stats import bartlett, levene
from numpy.random import rand
from numpy.random import seed
from scipy.stats import spearmanr

df = pd.read_csv('countries-table.csv')

data = pd.DataFrame(df)

print(data)

#testing for normality

statistics, p_value = stats.shapiro(data['area'].dropna())
print(statistics, p_value)

if (p_value>.05):
    print('Normal')
else:
    print('Not normal')

statistics, p_value = stats.shapiro(data['netChange'].dropna())
print(statistics, p_value)

if (p_value>.05):
    print('Normal')
else:
    print('Not normal')

statistics, p_value = stats.shapiro(data['growthRate'].dropna())
print(statistics, p_value)

if (p_value>.05):
    print('Normal')
else:
    print('Not normal')

statistics, p_value = stats.shapiro(data['worldPercentage'].dropna())
print(statistics, p_value)

if (p_value>.05):
    print('Normal')
else:
    print('Not normal')

print()

#ANOVA of a few countries' populations in 2024

popIn1980 = data['pop1980']
popIn2000 = data['pop2000']
popIn2010 = data['pop2010']
popIn2023 = data['pop2023']
popIn2024 = data['pop2024']

f, p = f_oneway(popIn1980,popIn2000,popIn2010,popIn2023,popIn2024)

print(f"ANOVA result between all populations in the different years: F = {f}, p = {p}")
if p < 0.05:
    print('Reject null hypothesis: at least one group mean is different')
else:
    print('Fail to reject null hypothesis: all group means are the same')

print()

allArea = data['area']

f, p = f_oneway(allArea, popIn2024)

print(f"ANOVA result between area and population in 2024: F = {f}, p = {p}")
if p < 0.05:
    print('Reject null hypothesis: at least one group mean is different')
else:
    print('Fail to reject null hypothesis: all group means are the same')

print()

allGrowthRates = data['growthRate']

f, p = f_oneway(allGrowthRates, popIn2024)

print(f"ANOVA result between growth rate and population in 2024: F = {f}, p = {p}")
if p < 0.05:
    print('Reject null hypothesis: at least one group mean is different')
else:
    print('Fail to reject null hypothesis: all group means are the same')

print()

allWorldPercetanges = data['worldPercentage']

f, p = f_oneway(allWorldPercetanges, allGrowthRates)

print(f"ANOVA result between growth rate and world percentage: F = {f}, p = {p}")
if p < 0.05:
    print('Reject null hypothesis: at least one group mean is different')
else:
    print('Fail to reject null hypothesis: all group means are the same')

print()

plt.scatter(allArea, popIn2024)
plt.show()

coef, p = spearmanr(allArea, popIn2024)
print('Spearmans correlation coefficient: %.3f' % coef)

alpha = 0.05
if p > alpha:
	print('Samples are uncorrelated (fail to reject H0) p=%.3f' % p)
else:
	print('Samples are correlated (reject H0) p=%.3f' % p)

print()

plt.scatter(allGrowthRates, popIn2024)
plt.show()

coef, p = spearmanr(allGrowthRates, popIn2024)
print('Spearmans correlation coefficient: %.3f' % coef)

alpha = 0.05
if p > alpha:
	print('Samples are uncorrelated (fail to reject H0) p=%.3f' % p)
else:
	print('Samples are correlated (reject H0) p=%.3f' % p)

print()

plt.scatter(allGrowthRates, allWorldPercetanges)
plt.show()

coef, p = spearmanr(allGrowthRates,allWorldPercetanges)
print('Spearmans correlation coefficient: %.3f' % coef)

alpha = 0.05
if p > alpha:
	print('Samples are uncorrelated (fail to reject H0) p=%.3f' % p)
else:
	print('Samples are correlated (reject H0) p=%.3f' % p)