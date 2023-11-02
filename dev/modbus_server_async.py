"""
Simulated Modbus Sensor Server -- in asynch mode

This Python module simulates a Modbus server providing sensor data for testing and development.
You can customize the simulated data to match your specific use case.

Author: Vikas Kumar Sinha
Date: October 31, 2023
License: NA

Use this code at your own risk. There is no warranty, implied or otherwise.
"""


import asyncio
from pymodbus.server.asynchronous import StartTcpServer
from pymodbus.datastore import ModbusSequentialDataBlock
from pymodbus.datastore import ModbusSlaveContext
from pymodbus.datastore import ModbusServerContext
import logging

# Configure the server logging
FORMAT = (
    "%(asctime)-15s %(threadName)-15s "
    "%(levelname)-8s %(module)-15s:%(lineno)-8s %(message)s"
)
logging.basicConfig(format=FORMAT)
log = logging.getLogger()
log.setLevel(logging.INFO)

SW_VERSION_REG_ADD = 0
MODBUS_TABLE_VERSION_REG_ADD = 1
MAC_ADDRESS_REG_START_ADD = 2
POWER_FACTOR_REG_START_ADD = 244
RMS_VOLTAGE_REG_START_ADD = 352
RMS_VOLTAGE_AVG_REG_START_ADD = 388
RMS_FREQ_REG_START_ADD = 424

MODBUS_SERVER_IP_ADDRESS = "127.0.0.1"
MODBUS_SERVER_PORT = 5021

async def create_simulated_modbus_server():
    # Simulate sensor data in data blocks for different registers
    sw_version_data_block = ModbusSequentialDataBlock(SW_VERSION_REG_ADD, [514])
    modbus_table_version_data_block = ModbusSequentialDataBlock(MODBUS_TABLE_VERSION_REG_ADD, [2])
    mac_add_data_block = ModbusSequentialDataBlock(MAC_ADDRESS_REG_START_ADD, [30, 44285, 17639])
    pwr_factor_data_block = ModbusSequentialDataBlock(POWER_FACTOR_REG_START_ADD, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    rms_voltage_data_block = ModbusSequentialDataBlock(RMS_VOLTAGE_REG_START_ADD, [49709, 17262, 20887, 15905, 45177, 15748, 0, 0, 0, 0, 0, 0])
    rms_voltage_avg_data_block = ModbusSequentialDataBlock(RMS_VOLTAGE_AVG_REG_START_ADD, [34030, 17262, 13400, 15907, 22707, 15748, 0, 0, 0, 0, 0, 0])
    freq_data_block = ModbusSequentialDataBlock(RMS_FREQ_REG_START_ADD, [54339, 16973, 54339, 16973, 43051, 16949, 0, 0, 0, 0, 0, 0])
    
    # Create a Modbus server context
    store = ModbusServerContext(single=True, slaves={1: ModbusSlaveContext()})

    # Register the data blocks in the server context
    store[1] = sw_version_data_block
    store[1] = modbus_table_version_data_block
    store[1] = mac_add_data_block
    store[1] = pwr_factor_data_block
    store[1] = rms_voltage_data_block
    store[1] = rms_voltage_avg_data_block
    store[1] = freq_data_block

    try:
        # Start the Modbus server on the specified IP address and port
        await StartTcpServer(context=store, address=(MODBUS_SERVER_IP_ADDRESS, MODBUS_SERVER_PORT))
        log.info(f"Simulated Modbus Server started at {MODBUS_SERVER_IP_ADDRESS}:{MODBUS_SERVER_PORT}")
    except Exception as e:
        log.info(f"Error starting Modbus Server: {str(e)}")

if __name__ == "__main__":
    # Entry point for running the simulated Modbus server.
    print("Starting Simulated Modbus Server...")
    asyncio.run(create_simulated_modbus_server())
