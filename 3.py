import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

first = pd.read_csv('1.txt', sep='\t', index_col=None, header=None, usecols=[1])
first = first.to_numpy()
# first = first.reshape((len(first) // 6), 6)
second = pd.read_csv('2.txt', sep='\t', index_col=None, header=None, usecols=[1])
second = second.to_numpy()
# second = second.reshape((len(second) // 6), 6)

first_x = pd.read_csv('1_x.txt', sep='\t', index_col=None, header=None, usecols=[1])
first_x = first_x.to_numpy()
# first_x = first_x.reshape((len(first_x) // 6), 6)
second_x = pd.read_csv('2_x.txt', sep='\t', index_col=None, header=None, usecols=[1])
# second_x.to_csv('1.csv', sep='\t', index=None, header=None)
second_x = second_x.to_numpy()


# second_x = second_x.reshape((len(second_x) // 6), 6)


def eqv(coord):
    # x1 = 0.05375000000000007
    # x2 = 0.30374999999999996
    # y1 = 3.4362206646776574
    # y2 = 8.66456712137057
    x1 = 0.
    x2 = 0.4050000000000001
    y1 = 1.
    y2 = 7.877165546567421
    return (y2 - y1) / (x2 - x1) * coord + y2 - (y2 - y1) / (x2 - x1) * x2


err = [float(np.abs((res - eqv(x)) / res)*100) for x, res in zip(second_x, second)]
print(np.average(err[7:]))

# sns.set_style("whitegrid")
# sns.set_palette("deep")
# sns.lineplot(x=[0.05375000000000007, 0.30374999999999996], y=[3.4362206646776574, 8.66456712137057],
#              label='Эксперимент'
#              )
# sns.scatterplot(x=first_x[:7, 0], y=first[:7, 0], label='[5]')
# sns.scatterplot(x=first_x[:7, 1], y=first[:7, 1], label='[8]')
# sns.scatterplot(x=first_x[:7, 2], y=first[:7, 2], label='[12]')
# sns.scatterplot(x=first_x[:7, 3], y=first[:7, 3], label='[15]')
# sns.scatterplot(x=first_x[:7, 4], y=first[:7, 4], label='[18]')
# sns.scatterplot(x=first_x[:7, 5], y=first[:7, 5], label='[21] ')
# plt.ylabel('Безразмерный перепад давления (Δpтр/Δp0)')
# plt.xlabel('Массовое паросодержание (X)')
# plt.show()
#
# sns.set_style("whitegrid")
# sns.set_palette("deep")
# sns.lineplot(x=[0., 0.4050000000000001], y=[1., 7.877165546567421],
#              label='Эксперимент'
#              )
# sns.scatterplot(x=second_x[1:, 0], y=second[1:, 0], label='[5]')
# sns.scatterplot(x=second_x[1:, 1], y=second[1:, 1], label='[8]')
# sns.scatterplot(x=second_x[1:, 2], y=second[1:, 2], label='[12]')
# sns.scatterplot(x=second_x[1:, 3], y=second[1:, 3], label='[15]')
# sns.scatterplot(x=second_x[1:, 4], y=second[1:, 4], label='[18]')
# sns.scatterplot(x=second_x[1:, 5], y=second[1:, 5], label='[21]')
# plt.ylabel('Безразмерный перепад давления (Δpтр/Δp0)')
# plt.xlabel('Массовое паросодержание (X)')
# plt.show()
