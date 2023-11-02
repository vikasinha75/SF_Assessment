"""
main.py: This is the start point of the execution of the code

This script reads data from the sensor, process it and then store to backend server

Author: Vikas Kumar
Date: October 31, 2023
"""

# Import necessary modules
import os
import sys
import threading
import logging
import asyncio

# import dev.modbus_server_synch as sensor
import sensor_operation.read_ecoadapt_test as sensor_read
import process_sensor_data as data_process
from simulated_sensor import SimulatedSensor
from process_sensor_data import ModbusDataReader

# configure the client logging
FORMAT = (
    "%(asctime)-15s %(threadName)-15s "
    "%(levelname)-8s %(module)-15s:%(lineno)-8s %(message)s"
)
logging.basicConfig(format=FORMAT)
log = logging.getLogger()
log.setLevel(logging.INFO)


def main_function():
    """
    Perform the main operation of the script.

    Args:
        None

    Returns:
        str: A message indicating the result of the operation.
    """

    # Fetch the data from simulated sensor
    reader = ModbusDataReader()
    rms_voltage_values = reader.read_rms_voltage(reader.RMS_VOLTAGE_REG_START_ADD)
    rms_freq_values = reader.read_rms_freq(reader.RMS_FREQ_REG_START_ADD)


    #----- Turn on the Modbus simulated server - basically sensor
    # log.info("Starting Simulated Modbus Server")
    # # Create a thread for running the Modbus server
    # sensor_thread = threading.Thread(target=sensor.create_simulated_modbus_server)
    # sensor_thread.daemon = True  # This allows the thread to exit when the main program ends
    # # Start the server thread
    # sensor_thread.start()
    # # Wait for the server to signal that it's ready
    # sensor.modbus_server_ready_event.wait()

    # # Perform other tasks in your application
    # print("Your application is running...")

    # #read the data from the sensor
    # sensor_read.run_sync_client()

    #process the data
    #store the data
    result = f"All is well :) "
    return result

def helper_function():
    """
    Perform a helper operation.

    This function performs a helper operation and returns a message.

    Returns:
        str: A message from the helper function.
    """
    return "Helper function executed successfully."

if __name__ == "__main__":
    # Get command-line arguments
    # arg1 = sys.argv[1] if len(sys.argv) > 1 else "default_value"
    # arg2 = int(sys.argv[2]) if len(sys.argv) > 2 else 0

    # Call the main function
    result = main_function()

    # Print the result
    print(result)
