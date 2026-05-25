import serial
import time

SERIAL_PORT = 'COM3'
BAUD_RATE = 9600

try: 
  arduino = serial.Serial(port=SERIAL_PORT, baudrate=BAUD_RATE, timeout = 1)

  print("Connecting to Arduino...")
  time.sleep(2)
  print("Connected successfully!\n")

  print("Type anything and press Enter to send it to the Arduino.")
  print("Type 'exit' to quit.")
  print("-" * 50)

  while True:
    user_input = input("You: ")

    if user_input.lower() == 'exit':
      print("Closing connection")
      break

    if not user_input.strip():
      continue

    data_to_send = user_input + '\n'
    arduino.write(data_to_send.encode('utf-8'))

except serial.SerialException as e:
  print(f"Error: Could not open serial port {SERIAL_PORT}. Is it plugged in?")
  print(e)

finally: 
  if 'ardunio' in locals() and arduino.is_open:
    arduino.close()
    print("Serial port is closed.")

