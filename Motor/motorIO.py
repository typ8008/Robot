try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print('Error Importing RPI.GPIO, Check if package installed or run application with "sudo"')

import motor

class MotorIO(motor.Motor):
    
    def __init__(self,direction_pin, speed_pin):
        """
        Set up speed pin GPIO to be Output, PWM
        and direction pin GPIO to be Output
        """
        super().__init__()
        # Set numbering pathern to be related to BCM    
        GPIO.setmode(GPIO.BCM)

        # Turn of warning display
        GPIO.setwarnings(False)

        # Set direction pin as Output
        GPIO.setup(direction_pin,GPIO.OUT)
        # Set speed pin as output
        GPIO.setup(speed_pin,GPIO.OUT)
        
        # Set speed pin as PWM with 100 Hz frequency
        self.motor = GPIO.PWM(speed_pin, 100)
        self.direction_pin = direction_pin
        
    def motor_stop(self):
        """
        Method to stop Motor/PWM
        """
        self.motor.stop()
        
    def motor_start(self):
        """
        Method to start Motor/PWM with zero speed
        """
        self.motor.start(0)

    def change_speed(self):
        """
        Method for changing speed/PWM duty cycle
        Speed taken from Parent Class
        """
        self.motor.ChangeDutyCycle(self.get_speed())
        
    def change_direction(self):
        """
        Method to change direction of the motor
        False - Forward, True - Reverse
        Direction value taken from Parent Class
        """
        if self.get_direction():
            GPIO.output(self.direction_pin,GPIO.HIGH)
        else:
            GPIO.output(self.direction_pin,GPIO.LOW)

class MotorA(MotorIO):
    """
    Helper class to make it easier for beginners to use modules
    """
    def __init__(self):
        """
        Initialise Parent Class with preset GPIO
        """
        super().__init__(21,12)
 
    def run(self, direction, speed):
        """
        Method to run Motor with given direction and speed
        """
        self.motor_start()
        self.set_direction(direction)
        self.set_speed(speed)
        self.change_direction()
        self.change_speed()
    
    def stop(self):
        """
        Method to stop motor
        """
        self.motor_stop()
    
    def adj_speed(self,speed):
        """
        Method to change Motor speed
        """
        self.set_speed(speed)        
        self.change_speed()

class MotorB(MotorIO):
    """
    Helper class to make it easier for beginners to use modules
    """    
    def __init__(self):
        """
        Initialise Parent Class with preset GPIO
        """
        super().__init__(22,13)
 
    def run(self, direction, speed):
        """
        Method to run Motor with given direction and speed
        """
        self.motor_start()
        self.set_direction(direction)
        self.set_speed(speed)
        self.change_direction()
        self.change_speed()
    
    def stop(self):
        """
        Method to stop motor
        """
        self.motor_stop()
    
    def adj_speed(self,speed):
        """
        Method to change Motor speed
        """
        self.set_speed(speed)        
        self.change_speed()

# Testing
if __name__ == "__main__":
    import time    
    motorA = MotorA()
    motorA.run(False, 70)
    time.sleep(5)
    motorA.adj_speed(90)
    time.sleep(5)
    motorA.stop()
    motorA.run(True,100)
    time.sleep(5)
    motorA.run(True,70)
    time.sleep(5)
    motorA.stop()
    motorA.run(False,0)