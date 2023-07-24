# Plotting BLEU scores for different models
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

TYPE = "CS"

scores = []

if TYPE == "BF":
    # BF
    scores1 = [85.58, 85.23, 87.31, 87.46, 87.5, 87.5, 87.34, 87.44, 87.35]
    scores2 = [87.07, 87.43, 87.54, 87.95, 87.78, 87.35, 87.59, 87.83]
    scores3 = [86.53, 88.15, 88.01, 87.92, 88.14, 88.23, 88.21, 88.09, 88.34, 88.26, 88.25, 88.31, 88.51, 88.26, 87.97, 88.26, 88.12]
    scores4 = [87.08, 86.37, 87.95, 87.34, 88.15, 86.43, 85.98, 85.48, 86.69]

    scores = scores1 + scores2 + scores3 + scores4

else:
    # CS
    scores1 = [11.05, 11.36, 11.84, 12.86, 13.42, 13.95, 13.81, 14.06, 14.01, 14.64, 14.54, 15.05, 15.42, 15.87, 15.85, 16.25, 16.82, 16.15, 15.83, 16.44, 16.26]
    scores2 = [16.95, 17.13, 17.08, 16.82, 16.82, 16.77]
    scores3 = [17.48, 17.3, 17.17, 17.02, 16.94]
    scores4 = [17.32, 17.15, 17.4, 17.07, 17.31, 17.28, 17.54, 17.58, 16.95, 17.4, 17.51, 17.75, 18.03, 18.11, 18.39, 17.5, 17.95, 18.66, 18.74, 18.53, 18.35, 18.75, 18.94, 18.34, 18.74, 18.43, 18.79]

    scores = scores1 + scores2 + scores3 + scores4

x = [i for i in range(1, len(scores)+1)]

sns.set_style("darkgrid")

# change the size of the plot
plt.figure(figsize=(10, 5))
plt.plot(x, scores, marker='o', color='lightcoral')

# change color of one of the points for each scores
plt.plot(len(scores1)-4, scores1[-5], marker='o', color='lightseagreen', markersize=10)
plt.annotate("Proceed with " + str(len(scores1)-4), (len(scores1)-4, scores1[-5]), xytext=(len(scores1)-9, scores1[-5]+0.4))
plt.plot(len(scores1)+len(scores2)-4, scores2[-5], marker='o', color='lightseagreen', markersize=10)
plt.annotate("Proceed with " + str(len(scores1)+len(scores2)-4), (len(scores1)+len(scores2)-4, scores2[-5]), xytext=(len(scores1)+len(scores2)-9, scores2[-5]+0.4))
plt.plot(len(scores1)+len(scores2)+len(scores3)-4, scores3[-5], marker='o', color='lightseagreen', markersize=10)
plt.annotate("Proceed with " + str(len(scores1)+len(scores2)+len(scores3)-4), (len(scores1)+len(scores2)+len(scores3)-4, scores3[-5]), xytext=(len(scores1)+len(scores2)+len(scores3)-9, scores3[-5]+0.4))
plt.plot(len(scores1)+len(scores2)+len(scores3)+len(scores4)-4, scores4[-5], marker='o', color='lightseagreen', markersize=10)
plt.annotate("Proceed with " + str(len(scores1)+len(scores2)+len(scores3)+len(scores4)-4), (len(scores1)+len(scores2)+len(scores3)+len(scores4)-4, scores4[-5]), xytext=(len(scores1)+len(scores2)+len(scores3)+len(scores4)-9, scores4[-5]+0.4))

# verical line
plt.axvline(x=len(scores1), color='lightcoral', linestyle='--')
plt.axvline(x=len(scores1)+len(scores2), color='lightcoral', linestyle='--')
plt.axvline(x=len(scores1)+len(scores2)+len(scores3), color='lightcoral', linestyle='--')
plt.axvline(x=len(scores1)+len(scores2)+len(scores3)+len(scores4), color='lightcoral', linestyle='--')


plt.xlabel('Early Stopping Epochs (We consider early stopping)')
plt.ylabel('BLEU Score')
plt.savefig(f'cl_merged_{TYPE}.png', bbox_inches='tight')