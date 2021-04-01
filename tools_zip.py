import subprocess as sp
def tar_gzip(file_location):
	
	output=sp.run(['tar','-xzvf',file_location],capture_output=True,text=True)
	output=output.stdout
	with open('output.txt','a') as f:
		f.write('\n\n the extracted files are:\n\n')
		for i in output:
			try:
				
				f.write(i)
			except TypeError:
				print('failed')


def tar_bzip2(file_location):
	
	output=sp.run(['tar','-xjvf',file_location],capture_output=True,text=True)
	output=output.stdout
	with open('output.txt','a') as f:
		f.write('\n\nthe extracted files are:\n\n')
		for i in output:
			try:
				
				f.write(i)
			except TypeError:
				print('failed')

def zipped(file_location):
	
	output=sp.run(['unzip','-n',file_location],capture_output=True,text=True)
	output=output.stdout
	with open('output.txt','a') as f:

		f.write('\n\nthe extracted files are in device:\n\n')
		for i in output:
			try:
				
				f.write(i)
			except TypeError:
				print('failed')

