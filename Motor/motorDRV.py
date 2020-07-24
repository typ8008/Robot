try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print('Error Importing RPI.GPIO, Check if package installed or run application with "sudo"')
    
import time

class DRV8832():
    
    def __init__(self,inA1, inA2, inB1, inB2, sleep, fault):
        """
        Set up speed pin GPIO to be Output, PWM
        and direction pin GPIO to be Output
        """
        #super().__init__()
        # Set numbering pathern to be related to BCM    
        GPIO.setmode(GPIO.BCM)

        # Turn of warning display
        GPIO.setwarnings(False)

        # Set direction pin as Output
        GPIO.setup(inA1,GPIO.OUT)
        # Set direction pin as Output
        GPIO.setup(inA2,GPIO.OUT)
        # Set direction pin as Output
        GPIO.setup(inB1,GPIO.OUT)
        # Set direction pin as Output
        GPIO.setup(inB2,GPIO.OUT)
        
        # Set direction pin as Output
        GPIO.setup(sleep,GPIO.OUT)
        # Set direction pin as Output
        GPIO.setup(fault,GPIO.IN)
        
        # Set speed pin as PWM with 100 Hz frequency
        self.motorA = GPIO.PWM(inA1, 100)
        self.directionA = inA2
        
        # Set speed pin as PWM with 100 Hz frequency
        self.motorB = GPIO.PWM(inB1, 100)
        self.directionB = inB2
        
        # set sleep pin
        self.sleep = sleep
        
        # set fault pin
        self.fault = fault
 
    def get_status(self):
        """
        Check if there is a Driver Fault
        """
        return GPIO.input(self.fault)
    
    def set_sleep_mode(self,mode):
        """
        Set sleep mode - False - Sleep, True - Run
        """
        GPIO.output(self.sleep, mode)
        
    def run(self, motor_id, direction, PWM):
        
        if PWM > 100 or PWM < 0:
            print ("PWM of range")
            return None
        
        if motor_id == "A":
            self.motorA.start(0)
            GPIO.output(self.directionA,direction)
            if direction:
                self.motorA.ChangeDutyCycle(100-PWM)
            else:
                self.motorA.ChangeDutyCycle(PWM)
        else:
            self.motorB.start(0)
            GPIO.output(self.directionB,direction)
            if direction:
                self.motorB.ChangeDutyCycle(100-PWM)
            else:
                self.motorB.ChangeDutyCycle(PWM)
    
    def stop(self, motor_id):
        """
        Method to stop motor
        """
        if motor_id == "A":
            self.motorA.stop()
            GPIO.output(self.directionA,False)
        else:
            self.motorB.stop()
            GPIO.output(self.directionB,False)
            
if __name__ == "__main__":
    motor = DRV8832(12,22,13,23,5,6)
    motor.run("B",True, 50)
    motor.run("A",True, 50)

    time.sleep(5)
    motor.stop("B")
    motor.stop("A")
