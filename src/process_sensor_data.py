"""
Data processor module for the ecoadapt sensor

This Python module prvides methods to convert data from hex to float etc.
You can customize the simulated data to match your specific use case.

Author: Vikas Kumar Sinha
Date: October 31, 2023
License: NA

Use this code at your own risk. There is no warranty, implied or otherwise.
"""

import struct
# from main import sensor
from simulated_sensor import SimulatedSensor



class ModbusDataReader:
    """
    This class allows you to interact with the sensor's data and convert it into SI units.
    """



    #Register addresses
    SW_VERSION_REG_ADD = 0
    MODBUS_TABLE_VERSION_REG_ADD = 1
    MAC_ADDRESS_REG_START_ADD = 2
    POWER_FACTOR_REG_START_ADD = 244
    RMS_VOLTAGE_REG_START_ADD = 352
    RMS_VOLTAGE_AVG_REG_START_ADD = 388
    RMS_FREQ_REG_START_ADD = 424
    #data size for electrical parameters
    ELECTRICAL_CONNECTORS = 2
    ELECTRICAL_CHANNELS = 3


    def __init__(self):
        # Initialize the Modbus communication here
        # You should have code to connect to the Modbus server
        self.rms_voltage = [0]*self.ELECTRICAL_CONNECTORS*self.ELECTRICAL_CHANNELS
        self.freq = [0]*self.ELECTRICAL_CONNECTORS*self.ELECTRICAL_CHANNELS
        self.sensor = SimulatedSensor()
        return

    def read_register(self, register_address):
        # Implement code to read the Modbus register
        # You should replace this with the actual code for reading the registers
        value = self.sensor.read_register(register_address)
        return value
    
    def read_rms_voltage(self, address):
        #read the voltage
        value = self.sensor.read_register(address)
        src_pointer = 0
        dest_pointer = 0
        for i in range(self.ELECTRICAL_CONNECTORS):
            for j in range(self.ELECTRICAL_CHANNELS):
                temp=self.unit_conversion(value[src_pointer], value[src_pointer + 1])
                # self.rms_voltage.append(temp)
                self.rms_voltage[dest_pointer] = temp
                src_pointer +=2
                dest_pointer +=1
                print(f"RMS Voltage - Con{i}Ch{j}: {temp}V\n")
                
        return self.rms_voltage

    def read_rms_freq(self, address):
        #read the voltage
        value = self.read_register(address)
        src_pointer = 0
        dest_pointer = 0
        for i in range(self.ELECTRICAL_CONNECTORS):
            for j in range(self.ELECTRICAL_CHANNELS):
                temp=self.unit_conversion(value[src_pointer], value[src_pointer + 1])
                self.freq[dest_pointer] = temp
                src_pointer +=2
                dest_pointer +=1
                print(f"Freq - Con{i}Ch{j}: {temp}Hz\n")
                
        return self.freq

    
    def unit_conversion(self, register1_decimal, register2_decimal):
        # Convert the decimal values to 16-bit big-endian hex strings
        hex_lsw = format(register1_decimal, '04X')
        hex_msw = format(register2_decimal, '04X')

        # Concatenate the two hex strings in the correct order (LSW first, then MSW)
        concatenated_hex = hex_msw + hex_lsw

        # Convert the concatenated hex string to a 32-bit float
        # Use the 'struct' module to pack and unpack binary data
        binary_data = bytes.fromhex(concatenated_hex)
        float_value = struct.unpack('!f', binary_data)[0]

        # Display the float32 value
        print("Float32 Value:", float_value)
        return float_value
        

if __name__ == "__main__":
    # Create an instance of ModbusDataReader
    # Read the data from simulated sensor
    
    reader = ModbusDataReader()

    # Read RMS_VOLTAGE and RMS_FREQ registers
    rms_voltage_values = reader.read_rms_voltage(reader.RMS_VOLTAGE_REG_START_ADD)
    rms_freq_values = reader.read_rms_freq(reader.RMS_FREQ_REG_START_ADD)

    # # Process and print voltage and frequency
    # voltage_str = reader.process_voltage(rms_voltage_values)
    # freq_str = reader.process_frequency(rms_freq_values)

    # print(f"RMS Voltage: {voltage_str}")
    # print(f"RMS Frequency: {freq_str}")