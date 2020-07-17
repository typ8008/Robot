class Motor:
    def __init__(self, speed=0, direction=False):
        """
        Motor Class, takes speed (0-100%) and direction (FWD - False, REV - True)
        """
        self.speed = speed;
        self.direction = direction;
        
    def get_speed(self):
        """
        Return speed 
        """
        return self.speed
    
    def get_direction(self):
        """
        Return Direction
        """
        return self.direction
    
    def set_speed(self, speed):
        """
        Set Speed
        """
        self.speed = speed
    
    def set_direction(self, direction):
        """
        Set Direction
        """
        self.direction = direction
