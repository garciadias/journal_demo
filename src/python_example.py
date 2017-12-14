import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

rep_path = os.getcwd()
dset = pd.read_csv("%s/data/m67_photometry.csv" % rep_path,
                   index_col=0)

fig = plt.figure(figsize=(9, 9))
ax = fig.add_subplot(111)
sns.kdeplot(dset.JK, dset.J, shade=True)
plt.ylim(18, 10)
plt.xlim(-0.15, 2)
plt.title('M67 2MASS', fontsize=18)
plt.show()
