import subprocess as sp
def exif(file_location):
	print('output from exiftool is:\n')
	output=sp.run(['exiftool',file_location],capture_output=True,text=True)
	print(output.stdout)


def bw(file_location):
	print('output from binwalk is:\n')
	output=sp.run(['binwalk',file_location],capture_output=True,text=True)
	print(output.stdout)



def strs(file_location):
	print('output from strings is:\n')
	output=sp.run(['strings',file_location],capture_output=True,text=True)
	print(output.stdout)



def xxd(file_location):
	print('output from xxd is:\n')
	output=sp.run(['xxd','-p',file_location],capture_output=True,text=True)
	print(output.stdout)



