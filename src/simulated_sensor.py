"""
Simulated Ecoadapt6 Sensor 

This Python module creates a dataset that looks like the sensor data. This is just for testing in absence
of real sensor and/or simulated modbus server

Author: Vikas Kumar Sinha
Date: Nov 02, 2023
License: NA

Use this code at your own risk. There is no warranty, implied or otherwise.
"""

class SimulatedSensor:
    """
    A class representing a simulated sensor with Modbus-like registers and data.
    This class allows you to interact with the sensor's data for testing and development purposes.
    """

    def __init__(self):
        self.sensor_data = {
            0: 514,  # SW_VERSION_REG_ADD
            1: 2,    # MODBUS_TABLE_VERSION_REG_ADD
            2: [30, 44285, 17639],  # MAC_ADDRESS_REG_START_ADD
            244: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # POWER_FACTOR_REG_START_ADD
            352: [49709, 17262, 20887, 15905, 45177, 15748, 0, 0, 0, 0, 0, 0],  # RMS_VOLTAGE_REG_START_ADD
            388: [34030, 17262, 13400, 15907, 22707, 15748, 0, 0, 0, 0, 0, 0],  # RMS_VOLTAGE_AVG_REG_START_ADD
            424: [54339, 16973, 54339, 16973, 43051, 16949, 0, 0, 0, 0, 0, 0],  # RMS_FREQ_REG_START_ADD
        }

    def read_register(self, address):
        """
        Read the value at the specified Modbus register address.

        Args:
            address (int): The Modbus register address.

        Returns:
            int or list: The value stored at the register address.
        """
        return self.sensor_data.get(address, None)

    def write_register(self, address, value):
        """
        Write a value to the specified Modbus register address.

        Args:
            address (int): The Modbus register address.
            value (int or list): The value to be written to the register.
        """
        if address in self.sensor_data:
            self.sensor_data[address] = value

if __name__ == "__main__":
    # Example usage of the SimulatedSensor class
    sensor = SimulatedSensor()

    print(sensor.read_register(0))  # Read SW_VERSION_REG_ADD
    sensor.write_register(1, 5)  # Write to MODBUS_TABLE_VERSION_REG_ADD
    print(sensor.read_register(1))  # Read MODBUS_TABLE_VERSION_REG_ADD

    # Iterate through the sensor data dictionary and print all key-value pairs
    for register_address, value in sensor.sensor_data.items():
        print(f"Register {register_address}: {value}")
