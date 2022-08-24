from pyfirmata import Arduino, util
import time

class camera(object):
	def __init__(self):
		self.angle = None
		
	def cameramoveleft(self):
		self.angle -= 1
		print("Moving camera left. Current camera angle: {0}".format(self.angle))
	
	def cameramoveright(self):
		self.angle += 1
		print("Moving camera right. Current camera angle: {0}".format(self.angle))
	
	def maxangle(self):
		print("Reached maximun angle!")