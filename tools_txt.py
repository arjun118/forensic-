
import subprocess as sp


def exif(file_location):
	print('output from exiftool is:\n')
	output=sp.run(['exiftool',file_location],capture_output=True,text=True)
	print(output.stdout)


def xxd(file_location):
	print('output from xxd is:\n')
	output=sp.run(['xxd','-p',file_location],capture_output=True,text=True)
	print(output.stdout)

def cat(file_location):
	output=sp.run(['cat',file_location]),capture_output=True,text=True)
	print(output.stdout)





