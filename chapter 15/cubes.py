import matplotlib.pyplot as plt

x_values = range(1, 5001)
y_values = [x**3 for x in x_values]
reversed_y_values = sorted(y_values, reverse=True)

plt.style.use('seaborn')
fig, ax = plt.subplots()

ax.scatter(x_values, y_values, c=reversed_y_values, cmap=plt.cm.YlOrRd, s=10)

# Set chart title and label axes.
ax.set_title('Cubic Numbers', fontsize=24)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Cube of Value', fontsize=14)

# Set the range for each axis.
ax.axis([0, 5050, 0, (5000**3)+10**9])

plt.show()