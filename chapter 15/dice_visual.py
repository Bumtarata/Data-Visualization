from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# Create two D6 die.
die_1 = Die()
die_2 = Die()

# Make some rolls and store results in a list.
number_of_rolls = 1_000_000
results = [die_1.roll() * die_2.roll() for roll_num 
    in range(number_of_rolls)]
    
# Analyze the results.
max_result = die_1.num_sides * die_2.num_sides
frequencies = [results.count(value) for value in range(1, max_result+1)]

# Visualize the results.
x_values = list(range(1, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title=f'Results of rolling two D{die_1.num_sides} '
    'and multiplying results instead of adding them together', 
    xaxis=x_axis_config, yaxis=y_axis_config, template='simple_white')
offline.plot({'data': data, 'layout': my_layout}, filename='2xD6.html')