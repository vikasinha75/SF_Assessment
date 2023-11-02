"""
Simulated Modbus Sensor Server

This Python module simulates a Modbus server providing sensor data for testing and development.
You can customize the simulated data to match your specific use case.

Author: Vikas Kumar Sinha
Date: October 31, 2023
License: NA

Use this code at your own risk. There is no warranty, implied or otherwise.
"""

# from pymodbus.server.asynchronous import StartTcpServer
# from pymodbus.datastore import ModbusSequentialDataBlock
# from pymodbus.datastore import ModbusServerContext
# from twisted.internet import reactor

from pymodbus.server.asynchronous import StartTcpServer
from pymodbus.datastore import ModbusSequentialDataBlock
from pymodbus.datastore import ModbusSlaveContext
from pymodbus.datastore import ModbusServerContext
from twisted.internet import reactor
import logging
import threading

# configure the server logging
FORMAT = (
    "%(asctime)-15s %(threadName)-15s "
    "%(levelname)-8s %(module)-15s:%(lineno)-8s %(message)s"
)
logging.basicConfig(format=FORMAT)
log = logging.getLogger()
log.setLevel(logging.INFO)

# Create an event to signal when the server is ready
modbus_server_ready_event = threading.Event()


SW_VERSION_REG_ADD = 0
MODBUS_TABLE_VERSION_REG_ADD = 1
MAC_ADDRESS_REG_START_ADD = 2
POWER_FACTOR_REG_START_ADD = 244
RMS_VOLTAGE_REG_START_ADD = 352
RMS_VOLTAGE_AVG_REG_START_ADD = 388
RMS_FREQ_REG_START_ADD = 424

MODBUS_SERVER_IP_ADDRESS = "127.0.0.1"
MODBUS_SERVER_PORT = 5021


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
        StartTcpServer(context=store, address=(MODBUS_SERVER_IP_ADDRESS, MODBUS_SERVER_PORT))
        log.info(f"Simulated Modbus Server started at {MODBUS_SERVER_IP_ADDRESS}:{MODBUS_SERVER_PORT}")
        # Signal that the server is ready
        modbus_server_ready_event.set()
    except Exception as e:
            log.info(f"Error starting Modbus Server: {str(e)}")


if __name__ == "__main__":
    """
    Entry point for running the simulated Modbus server.

    This script starts the simulated Modbus server when executed.
    """
    print("Starting Simulated Modbus Server...")
    create_simulated_modbus_server()
