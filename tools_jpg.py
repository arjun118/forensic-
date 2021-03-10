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
				print('failed')


def bw(file_location):
	
	output=sp.run(['binwalk',file_location],capture_output=True,text=True)
	output=output.stdout
	with open('output.txt','a') as f:
		f.write('\n\noutput from binwalk tool:\n\n')
		for i in output:
			try:
				
				f.write(i)
			except TypeError:
				print('failed')



def strs(file_location):
	
	output=sp.run(['strings',file_location],capture_output=True,text=True)
	output=output.stdout
	with open('output.txt','a') as f:
		f.write('\n\noutput from strings tool:\n\n')
		for i in output:
			try:
				
				f.write(i)
			except TypeError:
				print('failed')



def xxd(file_location):
	
	output=sp.run(['xxd','-p',file_location],capture_output=True,text=True)
	output=output.stdout
	with open('output.txt','a') as f:
		f.write('\n\noutput from xxd tool:\n\n')
		for i in output:
			try:
				
				f.write(i)
			except TypeError:
				print('failed')


def bulk_extractor(file_location):
	
	output=sp.run(['bulk_extractor','-o','data.dir',file_location],capture_output=True,text=True)
	output=output.stdout
	with open('output.txt','a') as f:
		f.write('\n\noutput from bulk_extractor tool:\n\n')
		f.write('\n\nsee the newly created dir for more info:\n\n')
		for i in output:
			try:
				
				f.write(i)
			except TypeError:
				print('failed')


def hashdeep(file_location):
	global output
	output=sp.run(['hashdeep',file_location],capture_output=True,text=True)
	output=output.stdout
	with open('output.txt','a') as f:
		f.write('output from hashdeep tool:\n\n')
		for i in output:
			try:
				
				f.write(i)
			except TypeError:
				print('failed')
	
