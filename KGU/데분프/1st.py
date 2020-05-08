# # input data
# ub = [11.35, 9.19, 10.3, 8.59, 4.98, 6.82, 6.03, 11.15, 9.38, 8.32, 8.34, 7.69, 13.58, 10.49,
#       11.07, 6.98, 9.77, 9.36, 8.39, 7.98, 6.56, 6.85, 8.06, 7.71, 11.04, 11.69, 9.4, 10,
#       5.45, 9.67, 8.93, 7.32, 13.70, 8.67, 10.08, 8.53, 9.14, 9.02, 6.7, 5.66, 8.26, 7.07,
#       12.23, 11.93, 4.76, 13.81, 11.41, 6.44, 9.5, 8.99]
#
# sb = [10.24, 6.16, 5.06, 10.64, 6.77, 10.13, 4.59, 1.38, 8.81, 1.97, 5.43, 6.32, 0.43, 7.3, 0.47,
#       10.82, 9.34, 2.39, 11.06, 4.19, 5.09, 8.2, 10.51, 1.94, 9.82, 6.69, 0.91, 6.17, 0.17, 7.47,
#       3.62, 2.23, 1.08, 9.16, 6.07, 7.51, 4.46, 2.13, 2.41, 7.24, 4.06, 7.7, 8.32, 6.33, 3.83,
#       4.96, 9.05, 6.41, 0.27, 8.48]
#
# import numpy as np
# from scipy import stats
#
# # calcuate mean of the samples
# mub, msb = np.mean(ub), np.mean(sb)
# print ("Mean value of ub and sb data are %.3f, %.3f respectively\n" %(mub, msb))
#
# # perform paired t-test
# tTestResult = stats.ttest_rel(ub, sb)
#
# print("The T-statistic is %.3f and the p-value is %.3f" % tTestResult)

# input data
# b = [10.02, 10.16, 9.96, 10.01, 9.87, 10.05, 10.07, 10.08, 10.05, 10.04, 10.09, 10.09, 9.92, 10.05, 10.13]
# a = [10.21, 10.16, 10.11, 10.10, 10.07, 10.13, 10.08, 10.30, 10.17, 10.10, 10.06, 10.37, 10.24, 10.19, 10.13]
#
# from scipy import stats
#
# # perform paired t-test
# tTestResult = stats.ttest_rel(b, a)
#
# print("The T-statistic is %.3f and the p-value is %.3f" % tTestResult)



# from scipy.stats import probplot
# import matplotlib.pyplot as plt
#
# # set parameter for plots
# f, axes = plt.subplots(1, 2, figsize=(12, 6))
# # draw the plots from data
# probplot(b, plot=axes[0])
# probplot(a, plot=axes[1])
# plt.show()

# input data
m1 = [185, 192, 201, 215, 170, 190, 175, 172, 198, 202]
m2 = [221, 210, 215, 202, 204, 196, 225, 230, 214, 217]

from scipy import stats
import matplotlib.pyplot as plt

# perform paired t-test
tTestResult = stats.ttest_rel(m1, m2)

print("The T-statistic is %.3f and the p-value is %.3f" % tTestResult)

# set parameter for plots
f, axes = plt.subplots(1, 2, figsize=(12, 6))
# draw the plots from data
axes[0].boxplot(m1)
axes[1].boxplot(m2)
plt.show()


# # perform shapiro-wilk test
# stest_m1, stest_m2 = stats.shapiro(m1), stats.shapiro(m2)
# print("p-values of shapiro-wilk test for \nm1: %.3f\nm2: %.3f"%(stest_m1[1],stest_m2[1]))