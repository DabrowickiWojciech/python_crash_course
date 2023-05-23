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
    
#Create a D6

die = Die()

#Make some rolls, and store results in a lsit.
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)
    
#print(results)

# Analize the results
frequencies = []
for value in range(1,die.num_sides+1):
    frequency = results.count(value)
    
    frequencies.append(frequency)
    
print(frequencies)

#Visualization
x_values = list(range(1, die.num_sides+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title':'Result'}
y_axis_config = {'title':'Frequency of Results'}

my_layout = Layout(title="Results", xaxis = x_axis_config, yaxis= y_axis_config)

offline.plot({'data':data, 'layout':my_layout}, filename='d6.html')
