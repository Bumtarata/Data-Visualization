import plotly.graph_objects as go
from plotly import offline

from random_walk import RandomWalk

# Make a random walk.
rw = RandomWalk(300_000)
rw.fill_walk()

# Visualize the results.
points = list(range(rw.num_points))
my_data = [go.Scattergl(x=rw.x_values, y=rw.y_values, mode='markers',
    marker=dict(
        color=points,
        colorscale='Blues',
        showscale=False,
        size=1)
    ),
    
    # highlight first and last step
    go.Scattergl(x=[0], y=[0], mode='markers', marker=dict(color='green', size=10)),
    go.Scattergl(x=[rw.x_values[-1]], y=[rw.y_values[-1]], mode='markers', 
        marker=dict(color='red', size=10)
        )
    ]
my_layout = go.Layout({'template': 'simple_white', 
                       'showlegend': False,
                       'xaxis': {'visible': False},
                       'yaxis': {'visible': False}
                    })
fig = go.Figure(data=my_data, layout=my_layout)
fig.show()