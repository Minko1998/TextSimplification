import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = pd.read_csv("randomvspos.csv")

groups = data.groupby('Description')
fig, ax = plt.subplots()

x_axis = 'Recall'
y_axis = 'Precision'
text = "The datapoints are corresponding to 1, 2, 3, 4, 5, 6 and 10 guessed words respectively."
plots = []
# sns.relplot(x = x_axis, y = y_axis, hue="Description", kind= 'line', data = group)
# sns



for name, group in groups:
    # sns.relplot(x = x_axis, y = y_axis, hue="Guesses", kind= 'line', data = group)
    ax.scatter(group[x_axis], group[y_axis], marker='.', linestyle='-', s=group['Guesses'] ** .5* 100, label=name)
    ax.plot(group[x_axis], group[y_axis], linestyle='-')
plt.title(f'The {y_axis} plotted to the {x_axis}')
plt.ylabel(y_axis)
plt.xlabel(x_axis)
plt.legend()
# plt.figtext(0.5, 0.01, text, wrap=True, horizontalalignment='center', fontsize=12)
plt.savefig(f'./images/randomPOS{x_axis}{y_axis}.png')