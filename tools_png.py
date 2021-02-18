#this module gives the different tools that we can 
#apply on png format files so that we can excract its contents
import subprocess as sp
def exif(file_location):
	print('output from exiftool is:\n')
	output=sp.run(['exiftool',file_location],capture_output=True,text=True)
	print(output.stdout)


def bw(file_location):
	print('output from binwalk is:\n')
	output=sp.run(['binwalk',file_location],capture_output=True,text=True)
	print(output.stdout)


def zsteg(file_location):
	print('output from zsteg is:\n')
	output=sp.run(['zsteg',file_location],capture_output=True,text=True)
	print(output.stdout)


def strs(file_location):
	print('output from strings is:\n')
	output=sp.run(['strings',file_location],capture_output=True,text=True)
	print(output.stdout)



def xxd(file_location):
	print('output from xxd is:\n')
	output=sp.run(['xxd','-p',file_location],capture_output=True,text=True)
	print(output.stdout)






#add xxd tool tomorrow.
#create similar modules for jpg and txt too.
#push the code tomorrow.


