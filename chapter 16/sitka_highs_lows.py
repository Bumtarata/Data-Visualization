import csv

from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    # Get dates, high and low temperatures from this file.
    dates, highs, lows = [], [], []
    date_index = header_row.index('DATE')
    high_index = header_row.index('TMAX')
    low_index = header_row.index('TMIN')
    name_index = header_row.index('NAME')
    name = None
    for row in reader:
        current_date = datetime.strptime(row[date_index], '%Y-%m-%d')
        try:
            high = int(row[high_index])
            low = int(row[low_index])
            if name == None:
                name = row[name_index]
                
        except ValueError:
            print(f'Missing data for {current_date}')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
            
    base_name = name[:-7].capitalize().split()
    first_part_of_name = []
    for word in base_name:
        first_part_of_name.append(word.capitalize())
    first_part_of_name = ' '.join(first_part_of_name)
    last_part_of_name = name[-7:].upper()
    full_name = first_part_of_name + last_part_of_name
    
    # Plot the high and low temperatures.
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(dates, highs, c='red', alpha=0.5)
    ax.plot(dates, lows, c='blue', alpha=0.5)
    ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
    
    # Format plot.
    ax.set_title(f'Daily high and low temperatures - 2018\n{full_name}',
        fontsize=20)
    ax.set_xlabel('', fontsize=16)
    fig.autofmt_xdate()
    ax.set_ylim(0, 135)
    ax.set_ylabel('Temperature (F)', fontsize=16)
    ax.tick_params(axis='both', which='major', labelsize=16)
    
    plt.show()