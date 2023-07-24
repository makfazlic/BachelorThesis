# Plotting BLEU scores for different models
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

TYPE = 'CS'

scores = []

if TYPE == 'BF':
    # BF
    scores = [78.71, 85.43, 86.88, 84.87, 87.58, 87.38, 87.83, 88.09, 87.9, 88.4, 88.5, 88.65, 88.37, 88.41, 88.51, 88.21]
    
else:
    # CS
    scores = [11.44, 12.81, 14.21, 15.02, 15.65, 15.51, 16.4, 16.96, 16.32, 17.08, 17.43, 17.71, 17.7, 17.52, 18.03, 17.71, 17.86, 18.21, 18.45, 18.52, 18.19, 18.4, 18.27, 18.07]

x = np.arange(1, len(scores)+1)

sns.set_style("darkgrid")

# change the size of the plot
plt.figure(figsize=(10, 5))
plt.plot(x, scores, marker='o', color='lightcoral')

# change color of one of the points
plt.plot(x[-5], scores[-5], marker='o', color='g')

# increase the size of the point
plt.plot(x[-5], scores[-5], marker='o', color='lightseagreen', markersize=10)
plt.annotate("Proceed with " + str(x[-5]), (x[-5], scores[-5]), xytext=(x[-5]-1, scores[-5]-1))


plt.xticks(x, x)
plt.xlabel('Early Stopping Epochs (We consider early stopping)')
plt.ylabel('BLEU Score')
plt.savefig(f'benchmark_merged_{TYPE}.png', bbox_inches='tight')