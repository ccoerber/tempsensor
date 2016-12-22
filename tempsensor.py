import time
import datetime
import serial
import getopt
import sys
import os

#################################################
# initialize the serial connection
#################################################
def initserial():
    devid = '/dev/ttyACM0'
    devrate = 9600
    ser = serial.Serial(devid, devrate)
    
    #TODO error handling
    return ser
 
#################################################
# return the current day of the month 
################################################# 
def getcurday():
    curdatetime = datetime.datetime.now()
    return curdatetime.day:
 
#################################################
# construct and return the filepath name for the 
# file used to store data
#################################################  
def buildfilepath(name):
    filepath = os.getcwd() + '\\tempdata'
    curdatetime = datetime.datetime.now()
    diryear = filepath + '\\' + str(curdatetime.year)
    if os.path.lexists(diryear) == False:
        os.mkdir(diryear)
    
    fileparts = [curdatetime.strftime('%d%m%y'), name, 'tempdata.csv']
    filepath = diryear + '\\' + '_'.join(fileparts)
    
    print "Using filepath " + filepath + "\n"
    return filepath

#################################################
# main function
#################################################    
if __name__ == "__main__":
  
    # -----------------------
    # get arguments
    # -----------------------
    try:
        opts, args = getopt.getopt(sys.argv[1:], "r:")
    except getopt.GetoptError as err:
        print str(err)
        sys.exit(2)
        
    for opt, arg in opts:
        if opt == '-r':
            roomname = arg
            
    
    curday = getcurday()
    outfile = open(buildfilepath(roomname), 'a')
   
    # -----------------------
    # initialize serial connection
    # -----------------------
    ser = initserial()
    
    # -----------------------
    # gather data
    # -----------------------
    while 1:
        data = ser.read(10)
        if data:
            outfile.write(data)
            outfile.flush()
     
        # don't check reading for certain number of seconds
        else:
            delayinsec = 25
            while delayinsec > 0:
                time.sleep(1)
                delayinsec = delayinsec - 1

            #next reading about to take place. Date changed?
            if curday != getcurday():
                curday = getcurday()
                outfile.close()
                outfile.open(buildfilepath(roomname), 'a')