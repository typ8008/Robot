from motorIO import MotorA, MotorB
import time
motorA = MotorA()
motorB = MotorB()

motorA.run(False, 70)
motorB.run(False, 100)

time.sleep(5)
motorA.adj_speed(90)
time.sleep(5)
motorA.stop()
motorB.stop()
motorA.run(True,100)
time.sleep(5)
motorA.run(True,70)
time.sleep(5)
motorA.stop()
motorA.run(False,0)
