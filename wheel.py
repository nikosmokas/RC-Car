from pyfirmata import Arduino, util
import time


class wheel(object):

	def __init__(self, name):
		self.name = name
		self.gear = None
		
	
	def forward(self):
		print('{0} is moving forwards in {1} gear!'.format(self.name, self.gear))
		
		
	def backward(self):
		print('{0} is moving backwards in {1} gear!'.format(self.name, self.gear))
		
	def left(self):
		if self.name == 'left':
			print('{0} is moving backwards in {1} gear!'.format(self.name, self.gear))
			
		elif self.name == 'right':
			print('{0} is moving forwards in {1} gear!'.format(self.name, self.gear))
			
	def right(self):
		if self.name == 'left':
			print('{0} is moving forwards in {1} gear!'.format(self.name, self.gear))
			
		elif self.name == 'right':
			print('{0} is moving backwards in {1} gear!'.format(self.name, self.gear))
			
	
	def stop(self):
		print('{0} stopped moving!'.format(self.name))
		
	