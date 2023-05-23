from random import randint
from plotly.graph_objs import Bar, Layout
from plotly import offline

class Die:
    """A class represanting a single die."""
    
    def __init__(self, num_sides=6):
        """Asume a six-sided die."""
        self.num_sides = num_sides
        
    def roll(self):
        """Return a random calue between 1 and number of sides."""
        return randint(1,self.num_sides)
    
#Create two D6

die1 = Die()
die2 = Die(10)

#Make some rolls, and store results in a lsit.
results = []
for roll_num in range(10000):
    result = die1.roll() + die2.roll()
    results.append(result)
    
#print(results)

# Analize the results
frequencies = []
max_results = die1.num_sides + die2.num_sides
for value in range(2,max_results+1):
    frequency = results.count(value)
    
    frequencies.append(frequency)
    
print(frequencies)

#Visualization
x_values = list(range(2, max_results+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title':'Result','dtick':1}
y_axis_config = {'title':'Frequency of Results'}

my_layout = Layout(title="Results", xaxis = x_axis_config, yaxis= y_axis_config)

offline.plot({'data':data, 'layout':my_layout}, filename='d6_d10.html')
