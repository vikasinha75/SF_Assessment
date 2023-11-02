"""
Simulated Modbus Sensor Server

This Python module simulates a Modbus server providing sensor data for testing and development.
You can customize the simulated data to match your specific use case.

Author: Vikas Kumar Sinha
Date: October 31, 2023
License: NA

Use this code at your own risk. There is no warranty, implied or otherwise.
"""

from pymodbus.server.asynchronous import StartTcpServer
from pymodbus.datastore import ModbusSequentialDataBlock
from pymodbus.datastore import ModbusServerContext
from twisted.internet import reactor

SW_VERSION_REG_ADD = 0
MODBUS_TABLE_VERSION_REG_ADD = 1
MAC_ADDRESS_REG_START_ADD = 2
POWER_FACTOR_REG_START_ADD = 244
RMS_VOLTAGE_REG_START_ADD = 352
RMS_VOLTAGE_AVG_REG_START_ADD = 388
RMS_FREQ_REG_START_ADD = 424

MODBUS_SERVER_IP_ADDRESS = "169.254.20.1"
MODBUS_SERVER_PORT = 502


def create_simulated_modbus_server():
    """
    Create a simulated Modbus server with sensor data.

    This function sets up a Modbus server and registers a data block with simulated
    sensor data. You can modify the data to simulate your specific sensor readings.

    Returns:
        None
    """

    # Simulate sensor data in a data block for following registers
        # Register 0, 1 word [514]
        # Register 1, 1 word [2]
        # Register 2, 3 words [30, 44285, 17639]
        # Register 244, 12 words [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        # Register 351, 12 words [49709, 17262, 20887, 15905, 45177, 15748, 0, 0, 0, 0, 0, 0]
        # Register 388, 12 words [34030, 17262, 13400, 15907, 22707, 15748, 0, 0, 0, 0, 0, 0]
        # Register 424, 12 words [54339, 16973, 54339, 16973, 43051, 16949, 0, 0, 0, 0, 0, 0]
    sw_version_data_block = ModbusSequentialDataBlock(SW_VERSION_REG_ADD, [514])
    modbus_table_version_data_block = ModbusSequentialDataBlock(MODBUS_TABLE_VERSION_REG_ADD, [2])
    mac_add_data_block = ModbusSequentialDataBlock(MAC_ADDRESS_REG_START_ADD, [30, 44285, 17639])
    pwr_factor_data_block = ModbusSequentialDataBlock(POWER_FACTOR_REG_START_ADD, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    rms_voltage_data_block = ModbusSequentialDataBlock(RMS_VOLTAGE_REG_START_ADD, [49709, 17262, 20887, 15905, 45177, 15748, 0, 0, 0, 0, 0, 0])
    rms_voltage_avg_data_block = ModbusSequentialDataBlock(RMS_VOLTAGE_AVG_REG_START_ADD, [34030, 17262, 13400, 15907, 22707, 15748, 0, 0, 0, 0, 0, 0])
    freq_data_block = ModbusSequentialDataBlock(RMS_FREQ_REG_START_ADD, [54339, 16973, 54339, 16973, 43051, 16949, 0, 0, 0, 0, 0, 0])
    
    # Create a Modbus server context and add the data blocks to it
    store = ModbusServerContext(slaves=1, single=True)
    store.register(sw_version_data_block, SW_VERSION_REG_ADD)
    store.register(modbus_table_version_data_block, MODBUS_TABLE_VERSION_REG_ADD)
    store.register(mac_add_data_block, MAC_ADDRESS_REG_START_ADD)
    store.register(pwr_factor_data_block, POWER_FACTOR_REG_START_ADD)
    store.register(rms_voltage_data_block, RMS_VOLTAGE_REG_START_ADD)  # Register block1 with address 352
    store.register(rms_voltage_avg_data_block, RMS_VOLTAGE_AVG_REG_START_ADD)  # Register block2 with add 388
    store.register(freq_data_block, RMS_FREQ_REG_START_ADD)  # Register block3  address 424

    # Start the Modbus server on localhost and port 502
    StartTcpServer(context=store, address=(MODBUS_SERVER_IP_ADDRESS, MODBUS_SERVER_PORT))

if __name__ == "__main__":
    """
    Entry point for running the simulated Modbus server.

    This script starts the simulated Modbus server when executed.
    """
    print("Starting Simulated Modbus Server...")
    create_simulated_modbus_server()
