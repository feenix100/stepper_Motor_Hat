import RPi.GPIO as GPIO
import time
from DRV8825 import DRV8825

def main():
    try:
        Motor1 = DRV8825(dir_pin=13, step_pin=19, enable_pin=12, mode_pins=(16, 17, 20))
        #Motor2 = DRV8825(dir_pin=24, step_pin=18, enable_pin=4, mode_pins=(21, 22, 27))
        num_iterations = 10


        motors = [Motor1]
        #step_angle = 1.8
        #total_angle = 30

        #steps = total_angle / step_angle

        for _ in range(num_iterations):

            for motor in motors:
                
                motor.SetMicroStep('softward', '1/8step')
                #see DRV8825 module fullstep, halfstep, 1/4step, 1/8step, 1/16step 1/32step
                time.sleep(.6)#adjust sleep time for quiet and smooth movement

                motor.TurnStep(Dir='backward', steps=20, stepdelay=0.005)#original value .005
                time.sleep(.5)#original value .5
                
                motor.TurnStep(Dir='forward', steps=20, stepdelay=0.005)#original value .005
                time.sleep(.5)
                
                motor.Stop()


            for motor in motors:
                motor.Stop()

    except Exception as e:
        
        GPIO.cleanup()
        
        print("Motor stop")
        
        for motor in motors:
            motor.Stop()
        exit()

if __name__ == "__main__":
    main()
