import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy import stats

file = r'data/ex8-42.xls'
df = pd.read_excel(file)
# print(df)

A = df['Machine A'][:5]
B = df['Machine B'][:5]
C = df['Machine C']
# print(A)

# plt.boxplot([A, B, C], sym="b*")
# plt.title('Boxplot for the diameter data')
# plt.xticks([1, 2, 3], ['A', 'B', 'C'])
# plt.show()

# f, axes = plt.subplots(1, 3, figsize=(100, 100))
# axes[0].hist(A, bins = 10)
# axes[1].hist(B, bins = 10)
# axes[2].hist(C, bins = 5)
# plt.axis("equal")
# plt.show()
#
# stat_a, p_a = stats.shapiro(A)
# stat_b, p_b = stats.shapiro(B)
# stat_c, p_c = stats.shapiro(C)
#
# print("p-vlaues for shapiro-wilk test are\nA: %f\nB: %f\nC: %f"%(p_a,p_b,p_c))
#
print("p-value for homogeneity of variance test is"
      ": %f"%(stats.fligner(B,C)[1]))
#
# k = []
# # k.append((np.std(A)**2)/np.mean(A)**2)
# k.append(((np.std(A))**2)/np.mean(A))
# # k.append(((np.std(B))**2)/(np.mean(B))**2)
# k.append(((np.std(A))**2)/np.mean(B))
# # k.append(((np.std(C))**2)/(np.mean(C))**2)
# k.append(((np.std(A))**2)/np.mean(C))
# print(k[:])
#
# _, p_anova = stats.f_oneway(A, B, C)
# print(p_anova)
#
# print("p-value for kruskal-wallis test between B, C: %f"%stats.kruskal(B,C)[1])
