import serial
print "Hello"

PORT = '/dev/ttyACM0'
BAUDRATE = 250000

with serial.Serial(PORT, BAUDRATE, timeout=1) as ser:
    # x = ser.read()          # read one byte
    # s = ser.read(10)        # read up to ten bytes (timeout)
    print("reading...")
    while True:
        line = ser.readline()   # read a '\n' terminated line
        data = [float(every_data) for every_data in line.split(',')[:-1]]
        print(data)