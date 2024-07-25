# Stepper Motor Hat for Raspberry Pi

### Overview

This repository provides comprehensive information about the Waveshare Stepper Motor Hat, designed for the Raspberry Pi. It facilitates the control of two stepper motors.

### Features

- **Control Two Stepper Motors**: The hat enables control of two stepper motors using a Raspberry Pi.
- **Python Script**: A Python script (`motor.py`) is available for motor control via the Waveshare Stepper Motor Hat.
- **DRV8825 Integration**: The `DRV8825.py` script is imported by `test.py` for enhanced motor control.
- **3D Printable Support**: The `rpiHatCylinder.stl` file is a 3D printable support for the hat, designed to connect to its corners using M2.5 screws.
- **Cooling Fan Compatibility**: The setup includes a GeeekPi cooling fan, requiring two stacker headers for installation on the Raspberry Pi 4.

### Power Requirements

- **Power Supply**: A 12V, 4A power supply is used to power the Motor Hat, Raspberry Pi 4, and NEMA 23 motor together.
- **Power Connection**: Connect the power supply to the DC barrel jack on the hat. The on/off switch on the hat will control power for both the Raspberry Pi and the hat. You can also plug a power adapter into both the Raspberry Pi and the hat simultaneously.

### Wiring and Configuration

- **Motor Wiring**: Refer to your motor's datasheet to ensure correct connection to A+ or A- terminals.
- **DIP Pins**: There are six metal pads on the bottom of the hat that can be bridged with solder, corresponding to the six DIP pins on the lower left corner of the hat.
  - **Step Mode**: Check `DRV8825.py` to adjust the steps (full step, half step, etc.) between hardware and software control. If using code to set step mode, set all DIP switches to 0. The first three switches affect the 1st motor, and the remaining three affect the 2nd motor.

### Additional Resources

- **Manual and Datasheet**: For more detailed instructions and technical specifications, refer to the [Waveshare Stepper Motor Hat Wiki](https://www.waveshare.com/wiki/Stepper_Motor_HAT). Note that some instructions may require interpretation.

### Example Script

```python
# motor.py
import DRV8825

# Your motor control code here
```

### 3D Print Support

- **STL File**: The `rpiHatCylinder.stl` file is available for 3D printing support structures for the hat.

By following these guidelines and utilizing the provided resources, you can effectively control stepper motors with the Waveshare Stepper Motor Hat on a Raspberry Pi.
