import subprocess
import os
import re

location=input('enter:')
if os.path.isfile(location):
    f1=subprocess.run(['file',location],capture_output=True,text=True)
    filetype=re.findall(r'\w+',f1.stdout)

    
    if ('PNG' in filetype):
        import tools_png
        tools_png.exif(location)
        tools_png.bw(location)
        tools_png.xxd(location)
        tools_png.strs(location)
        tools_png.zsteg(location)
        
    elif ('JPEG' in filetype):

        import tools_jpg
        tools_jpg.exif(location)
        tools_jpg.bw(location)
        tools_jpg.xxd(location)
        tools_jpg.strs(location)
        
    elif ('PDF' in filetype):
        import tools_pdf
        tools_pdf.exif(location)
        tools_pdf.bw(location)
        tools_pdf.xxd(location)
        tools_pdf.strs(location)


        
    


    elif ('text' in filetype):
        import tools_txt
        tools_txt.exif(location)
        tools_txt.xxd(location)
        tools_txt.cat(file_location)

    else:
        print('match')


else:
    print("CAUTION:file not found")
