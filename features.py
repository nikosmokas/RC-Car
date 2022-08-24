from pyfirmata import Arduino, util
import time
from pyfirmata.util import Iterator
from math import log

board = Arduino("COM4")


class wheel(object):

	def __init__(self, name, enablePin, forwardPin, backwardPin):
		self.name = name
		self.enablePin = board.get_pin('d:'+str(enablePin)+':o')
		self.forwardPin = board.get_pin('d:'+str(forwardPin)+':o')
		self.backwardPin = board.get_pin('d:'+str(backwardPin)+':o')
		self.gear = None
		
	def forward(self):
		#print('{0} is moving forwards!'.format(self.name))
		self.enablePin.write(1)
		self.forwardPin.write(1)
		self.backwardPin.write(0)
		
	def backward(self):
		#print(self.name+' is moving backwards!')
		self.enablePin.write(1)
		self.forwardPin.write(0)
		self.backwardPin.write(1)
	def left(self):
		if self.name == 'left':
		#	print(self.name+' is moving backwards (as it should be)!')
			self.enablePin.write(1)
			self.forwardPin.write(0)
			self.backwardPin.write(1)
		elif self.name == 'right':
			#print(self.name+' is moving forwards (as it should be)!')
			self.enablePin.write(1)
			self.forwardPin.write(1)
			self.backwardPin.write(0)
	def right(self):
		if self.name == 'left':
		#	print(self.name+' is moving forwards (as it should be)!')
			self.enablePin.write(1)
			self.forwardPin.write(1)
			self.backwardPin.write(0)
		elif self.name == 'right':
			#print(self.name+' is moving backwards (as it should be)!')
			self.enablePin.write(1)
			self.forwardPin.write(0)
			self.backwardPin.write(1)
	
	def stop(self):
		#print(self.name+' stopped moving!')
		self.enablePin.write(0)
		self.forwardPin.write(0)
		self.backwardPin.write(0)

class temperature(object):
	def __init__(self, tempPin):
		self.tempPin = board.get_pin('a:'+str(tempPin)+':i')
		
	def displaytemperature(self):
		iterator = Iterator(board)
		iterator.start()
		self.tempPin.enable_reporting()
		while True:
			if self.tempPin.read() == None:
				pass	
			else:
				voltage = float(self.tempPin.read()) * 5.0
				resistance = 10 * voltage / (5 - voltage)
				tempK = 1 / (log((resistance/10)) / 3950 + 1 / (273.15+25))
				tempC = int(tempK - 273.15)
				print("The temperature is " + str(tempC) + ' C!')
				self.tempPin.disable_reporting()
				iterator = None
				break
		return()

class horn(object):
	def __init__(self, hornPin):
		self.hornPin = board.get_pin('d:'+str(hornPin)+':o')
		
	def honk(self):
		self.hornPin.write(1)
	def honkrelease(self):
		self.hornPin.write(0)
		
class camera(object):
	def __init__(self, servoPin):
		self.servoPin = board.get_pin('d:'+str(servoPin)+':s')
		self.angle = None
		
	def cameramoveleft(self):
		self.angle -= 3
		#print("Moving camera left. Current camera angle: {0}".format(self.angle))
		self.servoPin.write(self.angle)
	
	def cameramoveright(self):
		self.angle += 3
		#print("Moving camera right. Current camera angle: {0}".format(self.angle))
		self.servoPin.write(self.angle)
		
	def maxangle(self):
		print("Reached maximun angle!")