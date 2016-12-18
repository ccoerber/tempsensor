import time
import datetime
import serial

if __name__ == "__main__":
  
  outfile = open('tempdata2.csv', 'a')
  
  ser = serial.Serial('COM2', 9600)
  while 1:
    data = ser.read(10)
    if data:
      #curtime = datetime.datetime.now()
      #strtime = curtime.strftime('%H:%M:%S')
      #print data
      outfile.write(data)
      outfile.flush()