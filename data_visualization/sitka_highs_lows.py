import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    #print(header_row)
    
    #for index, column_header in enumerate(header_row):
    #    print(index, column_header)
    
    #Get dates, high temperatures and low temperatures from this file.
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        high = (high-32)/1.8
        low = int(row[6])
        low = (low-32)/1.8
        dates.append(current_date)
        highs.append(high)
        lows.append(low)
        
#print(highs)
    
#Plot the high and low temperatures.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs, c = 'red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha = 0.5)
ax.fill_between(dates, highs, lows, facecolor = 'blue', alpha = 0.1)
 
#Format plot.
ax.set_title("Daily high and low temperatures - 2018, fontsize = 24")
ax.set_xlabel('Day',fontsize = 16)
fig.autofmt_xdate()
ax.set_ylabel('Temperature (C)',fontsize = 16)
ax.tick_params(axis='both', which = 'major', labelsize = 16)

plt.show()
    
    
    