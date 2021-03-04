import subprocess as sp


def exif(file_location):
	print('output from exiftool is:\n')
	output=sp.run(['exiftool',file_location],capture_output=True,text=True)
	output=output.stdout
	with open('output.txt','a') as f:
		f.write('\n\noutput from exif tool:\n\n')
		for i in output:
			try:
				
				f.write(i)
			except TypeError:
				print('Extracted')


def bw(file_location):
	print('output from binwalk is:\n')
	output=sp.run(['binwalk',file_location],capture_output=True,text=True)
	output=output.stdout
	with open('output.txt','a') as f:
		f.write('\n\noutput from binwalk tool:\n\n')
		for i in output:
			try:
				
				f.write(i)
			except TypeError:
				print('Extracted')



def strs(file_location):
	print('output from strings is:\n')
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
	print('output from xxd is:\n')
	output=sp.run(['xxd','-p',file_location],capture_output=True,text=True)
	output=output.stdout
	with open('output.txt','a') as f:
		f.write('\n\noutput from xxd tool:\n\n')
		for i in output:
			try:
				
				f.write(i)
			except TypeError:
				print('Extracted')


def peepdf(file_location):
	print('output from peepdf is:\n')
	output=sp.run(['xxd','-p',file_location],capture_output=True,text=True)
	output=output.stdout
	with open('output.txt','a') as f:
		f.write('\n\noutput from peepdf tool:\n\n')
		for i in output:
			try:
				
				f.write(i)
			except TypeError:
				print('Extracted')








