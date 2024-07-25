# Stepper Motor Hat for Raspberry Pi

### Overview

This repository provides detailed information about the Waveshare Stepper Motor Hat, compatible with the Raspberry Pi. This hat allows for the control of two stepper motors and includes all necessary resources and scripts.

### Features

- **Dual Motor Control**: Enables control of two stepper motors using the Raspberry Pi.
- **Python Scripts**: Includes `motor.py` for motor control and `DRV8825.py`, which is imported by `test.py`, for advanced motor control functionality.
- **3D Printable Support**: The `rpiHatCylinder.stl` file is a 3D printable support structure designed to secure the hat using M2.5 screws.
- **Cooling Fan Compatibility**: To accommodate a GeeekPi cooling fan, two stacker headers are required for installation on the Raspberry Pi 4.

### Power Configuration

- **Power Supply**: Use a 12V, 4A power supply to power the Motor Hat, Raspberry Pi 4, and NEMA 23 motor simultaneously.
- **Power Connection**: Connect the power supply to the DC barrel jack on the hat. The on/off switch on the hat will control power to both the Raspberry Pi and the hat. It is also possible to use separate power adapters for the Raspberry Pi and the hat concurrently.

### Wiring and Configuration

- **Motor Wiring**: Refer to your motor's datasheet to ensure correct wiring to A+ or A- terminals.
- **DIP Pins**: Six metal pads on the bottom of the hat can be bridged with solder to correspond to the six DIP pins on the lower left corner of the hat.
  - **Step Mode Adjustment**: Modify the step settings (full step, half step, etc.) in `DRV8825.py` for hardware or software control. If setting the step mode via code, ensure all DIP switches are set to 0. The first three switches control the 1st motor, while the remaining three control the 2nd motor.

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

By following these guidelines and utilizing the provided resources, you can effectively control stepper motors using the Waveshare Stepper Motor Hat with a Raspberry Pi.
