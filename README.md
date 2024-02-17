# stepperMotorHat
For the waveshare stepper motor hat compatible with raspberry pi

This repository contains information about the waveshare stepper motor hat for the raspberry pi. This allows control of two stepper motors. There is a python script - motor.py that can be used to control the motors using the waveshare stepper motor hat. DRV8825.py is imported by test.py.
The rpiHatCylinder.stl is 3d printable to provide support for the hat. It connects to the corners of the hat using a m2.5 screw I am using a geeekpi cooling fan so I needed to use two stacker headers to install the hat onto the rpi4. 

I used 12 volt, 4 amp power supply for the motor Hat, rpi4, and nema 23 motor together. Plug into dc barrel jack on the hat. There is an on/off switch on the hat it will power on/down the rpi as well as the hat. You can plug a power adapter into the rpi and hat at the same time.
Check the datasheet for your motor to make sure the wires are connected to A+ or A- correctly.

The 6 dip pins -
There are six metal pads on the bottom of the hat that can be bridged with solder, they correspond to the six dip pins on the lower left corner of the hat. 
 
Check the DRV8825.py to change the steps(fullstep, halfstep, etc) between hardware and software control(hardward and softward). If you are using code to set step mode, flip all dip switches to 0. The first 3 affect 1st motor, the other 3 affect 2nd motor.

See the wiki for the manual and datasheet. Some of the instructions may not make sense however.
https://www.waveshare.com/wiki/Stepper_Motor_HAT
