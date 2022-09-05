import json

# Explore the structure of the data.
filename = 'data/eq_data_30_day_20_04_2022.json'
with open(filename, encoding='utf8') as f:
    all_eq_data = json.load(f)

another_readable_file = 'data/another_readable_file.json'
with open(another_readable_file, 'w') as f:
    json.dump(all_eq_data, f, indent=4)