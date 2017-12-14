import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

rep_path = os.getcwd()
dset = pd.read_csv("%s/data/m67_photometry.csv" % rep_path, index_col=0)

sns.pairplot(dset, x_vars=['JK'], y_vars=['J'],
             hue='survey', size=9, plot_kws=dict(s=65))

plt.ylim(18, 5)
plt.xlim(-0.15, 2)
plt.show()
