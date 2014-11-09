from xbee import XBee
import serial, time, threading

class XbRssi:
   def __init__(self, serial_port): 
   	ser = serial.Serial(serial_port, 57600)
    	self.xbee = XBee(ser)
    	self.xbee.at(frame='A', command='MY', parameter='\x20\x01')
    	self.xbee.at(frame='B', command='CH', parameter='\x0e')
    	self.xbee.at(frame='C', command='ID', parameter='\x99\x99')

	self.updateThread = threading.Thread(target=self._rssi_loop)
	self.updateThread.daemon = True
	self.lastRSSI = 0

   def _rssi_loop(self):
	while True:
            self.xbee.send('at', frame_id='A', command='DB')
            response = xbee.wait_read_frame()
            self.lastRSSI = response.get('rssi')
            print "RSSI = -%d dBm" % ord(lastRSSI)
	    time.sleep(1)
	
   def getRssi(self):
	return self.lastRSSI
 
   def start(self):
	self.updateThread.start()
    
if __name__=='__main__':
   xb = XbRssi('/dev/ttyUSB0')
   xb.start()	
