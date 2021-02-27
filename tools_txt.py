
import subprocess as sp


def exif(file_location):
	print('output from exiftool is:\n')
	output=sp.run(['exiftool',file_location],capture_output=True,text=True)
	output=output.stdout
	with open('output.txt','a') as f:
		f.write('\n\noutput from exiftool:\n\n')
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
def cat(file_location):
	output=sp.run(['cat',file_location],capture_output=True,text=True)
	output=output.stdout
	with open('output.txt','a') as f:
		f.write('\n\noutput from cat command:\n\n')
		for i in output:
			try:
				
				f.write(i)
			except TypeError:
				print('Extracted')

