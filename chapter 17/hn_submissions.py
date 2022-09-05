from operator import itemgetter

import requests
from plotly.graph_objs import Figure, Bar

# Make an API call and store the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f'Status code: {r.status_code}')

# Process information about each submission.
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
    # Make a separate API call for each submission.
    url = f'https://hacker-news.firebaseio.com/v0/item/{submission_id}.json'
    r = requests.get(url)
    print(f'id: {submission_id}\tstatus: {r.status_code}')
    response_dict = r.json()
    
    # Build a dictionary for each article.
    if 'descendants' in response_dict:
        submission_dict = {
            'title': response_dict['title'],
            'hn_link': f'http://news.ycombinator.com/item?id={submission_id}',
            'comments': response_dict['descendants'],
        }
    else:
        submission_dict = {
            'title': response_dict['title'],
            'hn_link': f'http://news.ycombinator.com/item?id={submission_id}',
            'comments': 0,
        }
    submission_dicts.append(submission_dict)
    
submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
                            reverse=True)

# Visualize the data.
links, comments = [], []
for submission_dict in submission_dicts:
    name = submission_dict['title']
    url = submission_dict['hn_link']
    link = f'<a href="{url}">{name}</a>'
    comment = submission_dict['comments']
    if comment > 0:
        links.append(link)
        comments.append(submission_dict['comments'])

data = {
    'type': 'bar',
    'x': links,
    'y': comments,
    'marker': {'color': 'black'},
}
my_layout = {
    'title': {
        'text': 'The most active discussions currently happening on Hacker News',
        'x': 0.5,
        'font': {'size': 28,}
    },
    'xaxis': {
        'title': 'Submissions',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
    'yaxis': {
        'title': 'Number of Comments',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
    'hoverlabel': {'bgcolor': 'white', 'font': {'color': 'black'}},
}
fig = Figure(data=data, layout=my_layout)
fig.show()