import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

t_flow = np.array([568.36232, 569.71543, 571.06056, 572.39762, 573.72648,
                   575.04699, 576.3589, 577.662, 578.9561, 580.24102,
                   581.51659, 582.78267, 584.03915, 585.28589, 586.52265,
                   587.74915, 588.96514, 590.1704, 591.36475, 592.548])

t_wall = np.array([604.00651, 605.33832, 606.60996, 607.87355, 609.12471,
                   610.36197, 611.59067, 612.81061, 614.02159, 615.22346,
                   616.30705, 617.20911, 617.9942, 618.68918, 619.31854,
                   619.89741, 620.43417, 620.93491, 621.40354, 621.84094])

l = np.linspace(0.013947368421052632, 0.53 - 0.013947368421052632, 20)

exp_l_flow = [0, 0.530]
exp_t_flow = [294.5, 321]
exp_l_wall = [0.0668, 0.118, 0.166, 0.264, 0.316, 0.364, 0.414, 0.464]
exp_t_wall = [339, 341.5, 344, 348, 349, 349, 349, 349]

sns.set_style("whitegrid")
sns.set_palette("deep")
sns.lineplot(x=l, y=[341 for _ in range(20)], label='Линия температуры насыщения', color='green', linestyle='dashed')
sns.scatterplot(x=l, y=[t - 273.15 for t in t_flow], label='Температура воды, Korsar')
sns.lineplot(x=exp_l_flow, y=exp_t_flow, label='Температура воды, эксперимент', color='blue')
sns.scatterplot(x=l, y=[t - 273.15 for t in t_wall], label='Температура стенки, Korsar', color='orange')
sns.lineplot(x=exp_l_wall, y=exp_t_wall, label='Температура стенки, эксперимент', color='red')
plt.xlabel('Длина, м')
plt.ylabel('Температура, °C')
plt.legend()
plt.show()
