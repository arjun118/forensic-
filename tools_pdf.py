import subprocess as sp


def exif(file_location):
	
	output=sp.run(['exiftool',file_location],capture_output=True,text=True)
	output=output.stdout
	with open('output.txt','a') as f:

		f.write('\n\noutput from exif tool:\n\n')

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

		f.write('\n\noutput from binwalk tool:\n\n')

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

		f.write('\n\noutput from strings tool:\n\n')

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

		f.write('\n\noutput from xxd tool:\n\n')

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
				print('Extracted')












