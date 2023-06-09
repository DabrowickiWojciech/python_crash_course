class Settings:
    '''A class to store all settings for Alien Invasion.'''
    def __init__(self):
        #Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (6, 22, 66)
        
        #Ship settings
        self.ship_speed = 0.5
        self.ship_limit = 3
        
        #Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_heigth = 20
        self.bullet_color = (208,255,20)
        self.bullets_allowed = 2
        
        #Alien settings
        self.alien_speed = 0.2
        self.fleet_drop_speed = 8
        self.alien_points = 20
        
        #fleet direction of 1 represents right; -1 represents left
        self.fleet_direction = 1
        
        #How quickly the game speed up
        self.speedup_scale = 1.1
        
        #How quickly the alien point value increase
        self.score_scale = 1.5
        
        self.initialize_dynamic_settings()
    
    def initialize_dynamic_settings(self):
        '''Initialize settings that change throught the game.'''
        self.ship_speed = 0.5
        self.bullet_speed = 1.0
        self.alien_speed = 0.2
        
        #fleet_direction of 1 represents right; -1 represents left
        self.fleet_driection = 1
    
    def increase_speed(self):
        '''Increase speed settings and alien points values.'''
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        
        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)