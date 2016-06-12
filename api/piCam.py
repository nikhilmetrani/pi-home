import picamera
import os

def captureImage(fileName):
	print (fileName + " in capture Image")
	try:
    		camera = picamera.PiCamera()
    		camera.capture(fileName)
    		camera.close()
    		message = "Picture taken. Saving"
	except Exception as e :
		print e
    		message = "something went wrong. Try that again"
	return message

def captureAndUpdateLink(fileName, symLinkName):
	try:
		captureImage(fileName)
		if os.path.islink(symLinkName):
			os.unlink(symLinkName)
		os.symlink(fileName,symLinkName)
		message = "Picture taken. Saving"
	except Exception  as e:
		print e
    		message = "something went wrong. Try that again"
	return message
