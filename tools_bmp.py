import subprocess as sp
def exif(file_location):
	global output
	output=sp.run(['exiftool',file_location],capture_output=True,text=True)
	output=output.stdout
	with open('output.txt','w') as f:
		f.write('output from exiftool tool:\n\n')
		for i in output:
			try:
				
				f.write(i)
			except TypeError:
				print('Extracted')


def bw(file_location):
	global output
	output=sp.run(['binwalk',file_location],capture_output=True,text=True)
	output=output.stdout
	with open('output.txt','a') as f:
		f.write('output from binwalk tool:\n\n')
		for i in output:
			try:
				
				f.write(i)
			except TypeError:
				print('Extracted')


def zsteg(file_location):
	global output
	output=sp.run(['zsteg','-a',file_location],capture_output=True,text=True)
	output=output.stdout
	with open('output.txt','a') as f:
		f.write('output from zsteg tool:\n\n')
		for i in output:
			try:
				
				f.write(i)
			except TypeError:
				print('Extracted')


def strs(file_location):
	global output
	output=sp.run(['strings',file_location],capture_output=True,text=True)
	output=output.stdout
	with open('output.txt','a') as f:
		f.write('\n\noutput from strings tool:\n\n')
		for i in output:
			try:
				
				f.write(i)
			except TypeError:
				print('Extracted')



def xxd(file_location):
	global output
	output=sp.run(['xxd',file_location],capture_output=True,text=True)
	output=output.stdout
	with open('output.txt','a') as f:
		f.write('output from xxd tool:\n\n')
		for i in output:
			try:
				
				f.write(i)
			except TypeError:
				print('Extracted')