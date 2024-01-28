import matplotlib.pyplot as plt
import numpy as np

# Values
values = [[13516, 282], [2960,63], [500, 12]]

# Labels
labels = ["big", "medium", "small"]

# Create figure and axis
fig, ax = plt.subplots()

# Width of a bar 
width = 0.35       

# Setting position of bar on X axis
ind = np.arange(len(labels))

# Making the plot
rects1 = ax.bar(ind - width/2, [i[0] for i in values], width, label='Uncompressed')
rects2 = ax.bar(ind + width/2, [i[1] for i in values], width, label='DB Compressed')

# Adding labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Storage space (MB)')
ax.set_title('Storage space by compression type - InfluxDB')
ax.set_xticks(ind)
ax.set_xticklabels(labels)
ax.legend()

# Turn on the grid
ax.grid(True)

# Function to add a label on top of each bar
def autolabel(rects, percentages):
    for rect, percentage in zip(rects, percentages):
        height = rect.get_height()
        ax.annotate('{:.1f}%'.format(percentage),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

# Calculate percentages and add labels
percentages = [i[1] / i[0] * 100 for i in values]
autolabel(rects2, percentages)

plt.show()
