from random import choice
import matplotlib.pyplot as plt

class RandomWalk:
    """A classto generate random walks."""
    
    def __init__(self, num_points = 5000):
        """Initialize attributes of a walk."""
        self.num_points = num_points
        
        #All walks start at (0, 0).
        self.x_values = [0]
        self.y_values = [0]   
        
    def fill_walk(self):
        """Calculate all eht points in the walk."""
        
        #Keep taking steps until the walk reaches the desired length.
        while len(self.x_values) < self.num_points:
            
            #Decide which direction to go and how far to go in that direction.
            x_direction = choice([1,-1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance
            
            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            #Reject moves that go nowhere.
            if x_step == 0 and y_step == 0:
                continue
            
            #Calculate the new position.
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step
            
            self.x_values.append(x)
            self.y_values.append(y)
            
            
#Keep making nwe walks, as long as the program is active.
while True:
    #Make a random walk
    rw = RandomWalk(50_000)
    rw.fill_walk()

    #Plot the points in the walk.
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize = (10, 6), dpi = 128)
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c = point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=1)
    
    #Emphasize the first and last points.
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)    
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors = 'none', s = 100)
    
    #Removing the axis.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    
    plt.show()
    
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
