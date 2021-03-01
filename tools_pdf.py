import subprocess as sp


def exif(file_location):
	print('output from exiftool is:\n')
	output=sp.run(['exiftool',file_location],capture_output=True,text=True)
	output=output.stdout


def bw(file_location):
	print('output from binwalk is:\n')
	output=sp.run(['binwalk',file_location],capture_output=True,text=True)
	output=output.stdout



def strs(file_location):
	
	output=sp.run(['strings',file_location],capture_output=True,text=True)
	output=output.stdout



def xxd(file_location):
	
	output=sp.run(['xxd','-p',file_location],capture_output=True,text=True)
	output=output.stdout
	
def peepdf(file_location):
	
	output=sp.run(['peepdf',file_location],capture_output=True,text=True)
	output=output.stdout



