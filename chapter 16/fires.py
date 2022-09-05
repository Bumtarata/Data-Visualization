import csv

from decimal import Decimal

from plotly.graph_objs import Figure, Layout

filename = 'data/world_fires_1_day.csv'
with open(filename) as f:
    next(csv.reader(f)) # skip to the second row
    
    lats = []
    lons = []
    brightnesses = []

# Get data
    for row in csv.reader(f):
        lats.append(row[0])
        lons.append(row[1])
        brightnesses.append(Decimal(row[2]))
        
# Visualize the data
marker_size = []
for brightness in brightnesses:
    brightness = (brightness / 150) ** 3
    marker_size.append(brightness)
    
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': brightnesses,
    'marker': {
        'size': marker_size,
        'color': brightnesses,
        'colorscale': 'Inferno',
        'reversescale': False,
        'colorbar': {'title': 'Brightness'},
        'line.width': 0,
        }
    }]
my_layout = Layout(title={
    'text': 'World fires',
    'x': 0.5,
    })

fig = Figure(data=data, layout=my_layout)
fig.show()