import serial
import csv

# Replace 'COM3' with the actual port name of your Arduino
ser = serial.Serial("/dev/cu.usbserial-0001", 115200)

# Create a CSV file and write the header
csv_file = open('matrix_data_board2.csv', 'w', newline='')
csv_writer = csv.writer(csv_file)
header = ['Time'] + [f'Sensor_{i}' for i in range(9)]
csv_writer.writerow(header)

try:
    while True:
        try: 
            # Read a line from the serial port
            line = ser.readline().decode('utf-8').strip('\n\r')
            
            # Split the line
            values = line.split(', ')
            
            # Print the received data
            print(line)

            # Write the data to the CSV file
            csv_writer.writerow(values)
        except UnicodeDecodeError:
            print("UnicodeDecodeError: skipping line.")

except KeyboardInterrupt:
    # Close the serial port on Ctrl+C
    ser.close()
    csv_file.close()
    print("Serial port and CSV file closed.")