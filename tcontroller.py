from pynput import keyboard
import time
from features import wheel, temperature, horn, camera

print("Starting car... ")
	

leftwheel = wheel('left', 11, 5, 6)
rightwheel = wheel('right', 4, 9, 10)
cameraservo = camera(12)
temp = temperature(0)
Honk = horn(3)

for i in range(0,3):
	horn.honk(Honk)
	time.sleep(0.05)
	horn.honkrelease(Honk)
	time.sleep(0.05)

cameraservo.angle = 87
camera.cameramoveright(cameraservo)


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
	elif nkey[1:2] == 'h':
		horn.honk(Honk)
	elif nkey == 'Key.right':
		if cameraservo.angle >= 155:
			camera.maxangle(cameraservo)
		else: 
			camera.cameramoveright(cameraservo)
	elif nkey == 'Key.left':
		if cameraservo.angle <= 10:
			camera.maxangle(cameraservo)
		else:
			camera.cameramoveleft(cameraservo)
	
def on_release(key):
	nkey = str(key)
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
	elif nkey[1:2] == 'h':
		horn.honkrelease(Honk)
	elif nkey[1:2] == 't':
		temperature.displaytemperature(temp)
	elif nkey[0:3] == 'Key':
		pass
	elif nkey[1:2] == 'e':
		wheel.stop(leftwheel)
		wheel.stop(rightwheel)
		for i in range(0,2):
			horn.honk(Honk)
			time.sleep(0.05)
			horn.honkrelease(Honk)
			time.sleep(0.05)
		print('Shutting the engine...')
		exit()
		
with keyboard.Listener(on_press = on_press,
        on_release = on_release) as listener:
    listener.join()

