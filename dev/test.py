import struct

# Sample data read from Modbus registers in decimal format (both words in big-endian)
register1_decimal = 54339  # Example value for the first (least significant) register
register2_decimal = 16973  # Example value for the second (most significant) register

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



