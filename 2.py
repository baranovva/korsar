import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

X_1000 = np.array([0.1705951, 0.2560397, 0.3539139])
X_1500 = np.array([0.1042439, 0.1752433, 0.2290005])
X_2000 = np.array([0.0493108, 0.1032761, 0.175608])

qw_1000 = np.array([5.13640E+06, 4.40916E+06, 3.77277E+06])
qw_1500 = np.array([6.86370E+06, 4.68184E+06, 4.09100E+06])
qw_2000 = np.array([5.36370E+06, 5.68186E+06, 4.22737E+06])

ref_val_1000 = np.array([7.4E+06, 5.95E+06, 5.2E+06, 4.6E+06, 4.05E+06, 3.6E+06, 3.2E+06])
ref_val_1500 = np.array([7.25E+06, 5.5E+06, 4.6E+06, 4.05E+06, 3.55E+06, 3.05E+06])
ref_val_2000 = np.array([7.1E+06, 5.1E+06, 4.05E+06, 3.4E+06, 2.9E+06])
sns.set_style("whitegrid")
sns.set_palette("deep")
sns.scatterplot(x=X_1000, y=qw_1000, label='1000, Korsar', color='green')
sns.scatterplot(x=X_1500, y=qw_1500, label='1500, Korsar', color='blue')
sns.scatterplot(x=X_2000, y=qw_2000, label='2000, Korsar', color='red')
sns.scatterplot(x=np.arange(0, 0.7, 0.1), y=ref_val_1000, label='1000, эксперимент', marker='x', color='green')
sns.lineplot(x=np.arange(0, 0.7, 0.1), y=ref_val_1000, color='green', linestyle='dashed')
sns.scatterplot(x=np.arange(0, 0.6, 0.1), y=ref_val_1500, label='1500, эксперимент', marker='x', color='blue')
sns.lineplot(x=np.arange(0, 0.6, 0.1), y=ref_val_1500, color='blue', linestyle='dashed')
sns.scatterplot(x=np.arange(0, 0.5, 0.1), y=ref_val_2000, label='2000, эксперимент', marker='x', color='red')
sns.lineplot(x=np.arange(0, 0.5, 0.1), y=ref_val_2000, color='red', linestyle='dashed')
plt.xlabel('Массовое паросодержание')
plt.ylabel('Критический тепловой поток, Вт/М^2')
plt.legend()
plt.show()
