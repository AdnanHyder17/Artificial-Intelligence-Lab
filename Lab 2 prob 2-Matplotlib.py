# Use Matplotlib and perform following tasks:
# 1. Create a line chart consisting of 2 separate lines each having a label of its own and one of them styled
# in a doted manner. Also add labels to the axes.
# 2. Create a Pie Chart similar to the one given below. You can use dataset and colors of your own, but
# make sure that the structure is followed as is.

# Create a line chart
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y1 = [10, 15, 7, 12, 9]
y2 = [8, 11, 6, 14, 5]

plt.plot(x, y1, label='Line 1')
plt.plot(x, y2, linestyle='dotted', label='Line 2')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.legend()
plt.show()

# Create a Pie Chart
import matplotlib.pyplot as plt

# Sample data
labels = ['Food', 'Power', 'Grocery', 'Utilities', 'Entertainment']
sizes = [25, 30, 15, 20, 10]
colors = ['blue', 'green', 'orange', 'red', 'purple']
explode = (0.1, 0.1, 0.1, 0.1, 0.1)
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors, explode=explode)
ax.axis('equal')
plt.title('Monthly Expenses')
plt.show()
