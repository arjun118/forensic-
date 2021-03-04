import subprocess as sp


def exif(file_location):
	
	output=sp.run(['exiftool',file_location],capture_output=True,text=True)
	output=output.stdout
	with open('output.txt','a') as f:
<<<<<<< HEAD
		f.write('\n\noutput from exif tool:\n\n')
=======
		f.write('\n\noutput from exiftool :\n\n')
>>>>>>> baff5cf5438d30d9e3ee3da73405ecb73d6ed1c4
		for i in output:
			try:
				
				f.write(i)
			except TypeError:
				print('Extracted')
<<<<<<< HEAD
=======
	
>>>>>>> baff5cf5438d30d9e3ee3da73405ecb73d6ed1c4


def bw(file_location):
	
	output=sp.run(['binwalk',file_location],capture_output=True,text=True)
	output=output.stdout
	with open('output.txt','a') as f:
<<<<<<< HEAD
		f.write('\n\noutput from binwalk tool:\n\n')
=======
		f.write('\n\noutput from binwalk :\n\n')
>>>>>>> baff5cf5438d30d9e3ee3da73405ecb73d6ed1c4
		for i in output:
			try:
				
				f.write(i)
			except TypeError:
				print('Extracted')



def strs(file_location):
	
	output=sp.run(['strings',file_location],capture_output=True,text=True)
	output=output.stdout
	with open('output.txt','a') as f:
<<<<<<< HEAD
		f.write('\n\noutput from strings tool:\n\n')
=======
		f.write('\n\noutput from strings :\n\n')
>>>>>>> baff5cf5438d30d9e3ee3da73405ecb73d6ed1c4
		for i in output:
			try:
				
				f.write(i)
			except TypeError:
				print('Extracted')



def xxd(file_location):
	
	output=sp.run(['xxd','-p',file_location],capture_output=True,text=True)
	output=output.stdout
	with open('output.txt','a') as f:
<<<<<<< HEAD
		f.write('\n\noutput from xxd tool:\n\n')
=======
		f.write('\n\noutput from xxd :\n\n')
>>>>>>> baff5cf5438d30d9e3ee3da73405ecb73d6ed1c4
		for i in output:
			try:
				
				f.write(i)
			except TypeError:
				print('Extracted')
<<<<<<< HEAD


def peepdf(file_location):
	print('output from peepdf is:\n')
	output=sp.run(['xxd','-p',file_location],capture_output=True,text=True)
	output=output.stdout
	with open('output.txt','a') as f:
		f.write('\n\noutput from peepdf tool:\n\n')
=======
	
def peepdf(file_location):
	
	output=sp.run(['peepdf',file_location],capture_output=True,text=True)
	output=output.stdout
	with open('output.txt','a') as f:
		f.write('\n\noutput from peepdf :\n\n')
>>>>>>> baff5cf5438d30d9e3ee3da73405ecb73d6ed1c4
		for i in output:
			try:
				
				f.write(i)
			except TypeError:
				print('Extracted')
<<<<<<< HEAD





=======
>>>>>>> baff5cf5438d30d9e3ee3da73405ecb73d6ed1c4



