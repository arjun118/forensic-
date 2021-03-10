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
				print('failed')


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
				print('failed')


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
				print('failed')


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
				print('failed')



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
				print('failed')


ef bulk_extractor(file_location):
	
	output=sp.run(['bulk_extractor','-o','data.dir',file_location],capture_output=True,text=True)
	output=output.stdout
	with open('output.txt','a') as f:
		f.write('\n\noutput from bulk_extractor tool:\n\n')
		f.write('\n\nsee the newly created dir for more info:\n\n')
		for i in output:
			try:
				
				f.write(i)
			except TypeError:
				print('the extracted data from this tool needs to be inspected manually')

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