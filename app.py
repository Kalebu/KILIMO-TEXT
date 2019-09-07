import time
import serial
#import gammu
#import gammu.exception
import threading

class kilimo_text:

	def __init__(self):
		#===================initializing phone============
		#self.phone = gammu.StateMachine()
		#self.phone.ReadConfig()
		#self.Init()
	
		#===============initializing serial communication with arduino===============		
		self.baudrate = 9600
		self.signal_sender = None
		self.received_signal = None  		
		self.legend = serial.Serial('/dev/ttyACM0', baudrate)
		
		self.response = None
		self.sms_receive_Thread()
		
	def send_sms(self,phone, sms='test'):
		message = {
				'Text':sms,
				'SMSC':{'Location':1},
				'Number':phone}
		#self.phone.SendSMS(message)
		print("Message_sent")
		

	def delete_sms(self):
		for text in range(1, 10):
			try:
				#self.phone.DeleteSMS(Folder=1, location=text)
			except gammu.exception.ERR_EMPTY:
				break
	
	def get_sms(self):
		while True:
			self.delete_sms()		
			text = 1
			for text in range (1, 10):
				while True:
					try:
						self.sms = self.phone.GetSMS(Folder=1, Location=text)
						self.phone_number = self.sms[0]['Number']
						self.message_received = self.sms[0]['Text']
						self.message_received = self.message_received.lower()
						self.response = [self.phone_number, self.message_received]
						print(self.response)				
						break
					except gammu.exception.ERR_EMPTY:
						continue
				
		 	
	def receive_sms_Thread(self):
		self.recieve_sms_thread = threading.Thread(target = self.get_sms)
		self.receive_sms_thread.daemon = True
		self.receive_sms_thread.start()
		#self.receive_sms_thread.join()
	
	def receive_signal(self):
		if self.response:
			response = self.response
			self.response = None
			return response
	
	def signal_check(self):
		self.signal = int()
		if self.legend.in_waiting:
			self.signal = int()
			self.value = self.legend.read(size=1)
			self.signal = self.signal.from_bytes(self.value, byteorder='little')
			return signal
		return signal

	def send_signal(self, signal_reference):
		if signal_reference:
			try:
				self.legend.write(signal_reference.to_bytes(length=3, byteorder='little'))
			except Exception as ex:
				print(ex)
		


	def neurocore(self):
		self.send_sms(phone='0757294146')
		while True:
			checked_signal = self.signal_check()
			if checked_signal:
				print(checked_signal)
			checked_received = self.receive_signal
			if self.receive_signal:
				print(checked_received)
		
	#checking input from arduino
	#checking input from sms
	#returning response back to arduino
	 

lumina = kilimo_text()
if __name__ == '__main__':
	lumina.neurocore()
