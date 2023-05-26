import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'data/death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    #print(header_row)
    
    #for index, column_header in enumerate(header_row):
    #    print(index, column_header)
    
    #Get dates, high temperatures and low temperatures from this file.
    dates, highs, lows, precipitations = [], [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            precipitation = float(row[3])
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            high = (high-32)/1.8
            low = (low-32)/1.8
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
            precipitations.append(precipitation)
            
#print(highs)
    
#Plot the high and low temperatures.
plt.style.use('seaborn-v0_8')
fig1, ax1 = plt.subplots()
ax1.plot(dates, highs, c = 'red', alpha= 0.5)
ax1.plot(dates, lows, c='blue', alpha = 0.5)
ax1.fill_between(dates, highs, lows, facecolor = 'blue', alpha = 0.1)
 
#Format plot.
ax1.set_title("Daily high and low temperatures - 2018\nDeath Valley, CA", fontsize = 20)
ax1.set_xlabel('Day',fontsize = 16)
fig1.autofmt_xdate()
ax1.set_ylabel('Temperature (C)',fontsize = 16)
ax1.tick_params(axis='both', which = 'major', labelsize = 16)

#Plot the rainfall
fig2, ax2 = plt.subplots()
ax2.plot(dates, precipitations, '--', c = 'black', alpha = 0.5)

#Format plot
ax2.set_title("Daily rainfall - 2018\nDeath Valley, CA", fontsize = 20)
ax2.set_xlabel('Day', fontsize = 16)
fig2.autofmt_xdate()
ax2.set_ylabel('[mm] of rainfall', fontsize = 16)
ax2.tick_params(axis='both', which = 'major', labelsize = 20)

plt.show()
    
    
    