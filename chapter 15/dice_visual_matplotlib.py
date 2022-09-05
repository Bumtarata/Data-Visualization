import matplotlib.pyplot as plt

from die import Die

# Create two D6 die.
die_1 = Die()
die_2 = Die()

# Make some rolls and store results in a list.
number_of_rolls = 10_000
results = [die_1.roll() + die_2.roll() for roll_num in range(number_of_rolls)]
    
# Analyze the results.
max_result = die_1.num_sides + die_2.num_sides
min_result = 2 # number of dice
frequencies = list(results.count(value) for value in range(min_result, max_result+1))

# Visualize the results.
x_values = list(range(min_result, max_result+1))

fig, ax = plt.subplots()
ax.bar(x_values, frequencies, width=0.5, edgecolor='white', 
    linewidth=0.8 )
ax.set(xlim=(1.25, max_result+0.75), xticks=x_values,
    xlabel='Result', ylabel='Number of Results',
    title='Results of rolling two D6 10.000 times')
plt.show()