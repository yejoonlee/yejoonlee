import matplotlib.pyplot as plt
import pandas as pd
# import numpy as np
from scipy import stats

file = r'data/ex8-6.xls'
df = pd.read_excel(file)
# print(df)

A = df.Response[:6]
B = df.Response[6:12]
C = df.Response[12:18]
D = df.Response[18:24]

# plt.boxplot([A, B, C, D], sym="b*")
# plt.title('Boxplot for the soil PH data')
# plt.xticks([1, 2, 3, 4], ['A', 'B', 'C', 'D'])
# plt.show()
#
# f, axes = plt.subplots(1, 4, figsize=(100, 100))
# # axes[0].hist(A, bins = 10)
# stats.probplot(A, plot=axes[0]) #scipy.stats.probplot
# # axes[1].hist(B, bins = 10)
# stats.probplot(B, plot=axes[1]) #scipy.stats.probplot
# # axes[2].hist(C, bins = 10)
# stats.probplot(C, plot=axes[2]) #scipy.stats.probplot
# # axes[3].hist(D, bins = 10)
# stats.probplot(D, plot=axes[3]) #scipy.stats.probplot
# plt.axis("equal")
# plt.show()

# stat_a, p_a = stats.shapiro(A)
# stat_b, p_b = stats.shapiro(B)
# stat_c, p_c = stats.shapiro(C)
# stat_c, p_d = stats.shapiro(D)
#
# print("p-vlaues for shapiro-wilk test are\nA: %f\nB: %f\nC: %f\nD: %f"%(p_a,p_b,p_c,p_d))
#
# print("\nand p-values for homogeneity of variance test are"
#       "\nbartlett: %f\nlevene: %f\nfligner: %f"%(stats.bartlett(A,B,C,D)[1]
#                                                  , stats.levene(A,B,C,D)[1]
#                                                  , stats.fligner(A,B,C,D)[1]))
#
# k = []
# k.append((np.std(A)**2)/np.mean(A)**2)
# # k.append(((np.std(A))**2)/np.mean(A))
# k.append(((np.std(B))**2)/(np.mean(B))**2)
# # k.append(((np.std(A))**2)/np.mean(B))
# k.append(((np.std(C))**2)/(np.mean(C))**2)
# # k.append(((np.std(A))**2)/np.mean(C))
# k.append(((np.std(D))**2)/(np.mean(D))**2)
# # k.append(((np.std(A))**2)/np.mean(D))
#
# # print(k[:])

_, p_anova = stats.f_oneway(A, B, C, D)
print("p-value for ANOVA test: %f"%p_anova)

print("\np-value for kruskal-wallis test: %f"%stats.kruskal(A,B,C,D)[1])
