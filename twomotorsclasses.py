from pynput import keyboard
import time
from wheel import wheel
from cameracontrol import camera

print("Starting car... ")
print("Put a gear to move!")

#gear = input("Enter gear 1-3: ")

leftwheel = wheel('left')
rightwheel = wheel('right')
cameraservo = camera()

leftwheel.gear = 0
rightwheel.gear = 0
cameraservo.angle = 90

def on_press(key):
	nkey = str(key)
	if nkey[1:2] == 'w':
		wheel.forward(leftwheel)
		wheel.forward(rightwheel)
	elif nkey[1:2] == 's':
		wheel.backward(leftwheel)
		wheel.backward(rightwheel)
	elif nkey[1:2] == 'd':
		wheel.right(leftwheel)
		wheel.right(rightwheel)
	elif nkey[1:2] == 'a':
		wheel.left(leftwheel)
		wheel.left(rightwheel)
	elif nkey == 'Key.right':
		if cameraservo.angle == 180:
			camera.maxangle(cameraservo)
		else: 
			camera.cameramoveright(cameraservo)
	elif nkey == 'Key.left':
		if cameraservo.angle == 0:
			camera.maxangle(cameraservo)
		else:
			camera.cameramoveleft(cameraservo)
		
def on_release(key):
	nkey = str(key)
	print(nkey)
	if nkey[1:2] == 's':
		wheel.stop(leftwheel)
		wheel.stop(rightwheel)
	elif nkey[1:2] == 'w':
		wheel.stop(leftwheel)
		wheel.stop(rightwheel)
	elif nkey[1:2] == 'd':
		wheel.stop(leftwheel)
		wheel.stop(rightwheel)
	elif nkey[1:2] == 'a':
		wheel.stop(leftwheel)
		wheel.stop(rightwheel)
	elif nkey[1:2] == '0':
		rightwheel.gear = 0
		leftwheel.gear = 0
		print(rightwheel.gear)
	elif nkey[1:2] == '1':
		rightwheel.gear = 1
		leftwheel.gear = 1
		print(rightwheel.gear)
	elif nkey[1:2] == '2':
		rightwheel.gear = 2
		leftwheel.gear = 2
		print(rightwheel.gear)
	elif nkey[1:2] == '3':
		rightwheel.gear = 3
		leftwheel.gear = 3
		print(rightwheel.gear)
	elif nkey[0:3] == 'Key':
		pass
	elif nkey[1:2] == 'e':
		wheel.stop(leftwheel)
		wheel.stop(rightwheel)
		print('Shutting the engine...')
		exit()


with keyboard.Listener(on_press = on_press, 
		on_release = on_release) as listener:
    listener.join()

