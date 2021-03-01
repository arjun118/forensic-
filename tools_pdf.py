import subprocess as sp


def exif(file_location):
	
	output=sp.run(['exiftool',file_location],capture_output=True,text=True)
	output=output.stdout
	with open('output.txt','a') as f:
		f.write('\n\noutput from exiftool :\n\n')
		for i in output:
			try:
				
				f.write(i)
			except TypeError:
				print('Extracted')
	


def bw(file_location):
	
	output=sp.run(['binwalk',file_location],capture_output=True,text=True)
	output=output.stdout
	with open('output.txt','a') as f:
		f.write('\n\noutput from binwalk :\n\n')
		for i in output:
			try:
				
				f.write(i)
			except TypeError:
				print('Extracted')



def strs(file_location):
	
	output=sp.run(['strings',file_location],capture_output=True,text=True)
	output=output.stdout
	with open('output.txt','a') as f:
		f.write('\n\noutput from strings :\n\n')
		for i in output:
			try:
				
				f.write(i)
			except TypeError:
				print('Extracted')



def xxd(file_location):
	
	output=sp.run(['xxd','-p',file_location],capture_output=True,text=True)
	output=output.stdout
	with open('output.txt','a') as f:
		f.write('\n\noutput from xxd :\n\n')
		for i in output:
			try:
				
				f.write(i)
			except TypeError:
				print('Extracted')
	
def peepdf(file_location):
	
	output=sp.run(['peepdf',file_location],capture_output=True,text=True)
	output=output.stdout
	with open('output.txt','a') as f:
		f.write('\n\noutput from peepdf :\n\n')
		for i in output:
			try:
				
				f.write(i)
			except TypeError:
				print('Extracted')



