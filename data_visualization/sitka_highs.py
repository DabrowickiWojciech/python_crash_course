import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'data/sitka_weather_07_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    #print(header_row)
    
    #for index, column_header in enumerate(header_row):
    #    print(index, column_header)
    
    #Get dates and high temperatures from this file.
    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        high = (high-32)/1.8
        dates.append(current_date)
        highs.append(high)
        
#print(highs)
    
#Plot the high temperatures.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs, c = 'red')
 
#Format plot.
ax.set_title("Daily high temperatures, July 2018, fontsize = 24")
ax.set_xlabel('Day',fontsize = 16)
fig.autofmt_xdate()
ax.set_ylabel('Temperature (C)',fontsize = 16)
ax.tick_params(axis='both', which = 'major', labelsize = 16)

plt.show()
    
    
    