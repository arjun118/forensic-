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
        tools_png.bulk_extractor(location)
        
    elif ('JPEG' in filetype):

        import tools_jpg
        tools_jpg.exif(location)
        tools_jpg.bw(location)
        tools_jpg.xxd(location)
        tools_jpg.strs(location)
        tools_jpg.bulk_extractor(location)
        
    elif ('PDF' in filetype):
        import tools_pdf
        tools_pdf.exif(location)
        tools_pdf.bw(location)
        tools_pdf.xxd(location)
        tools_pdf.strs(location)
        tools_pdf.peepdf(location)
        tools_pdf.bulk_extractor(location)
        tools_pdf.pdf_parser(location)
        tools_pdf.pdfid(location)

    elif ('BMP' in filetype):

        import tools_bmp
        tools_bmp.exif(location)
        tools_bmp.bw(location)
        tools_bmp.xxd(location)
        tools_bmp.strs(location)
        tools_bmp.zsteg(location)
        tools_bmp.bulk_extractor(location)

    elif ('gzip' in filetype):

        import tools_zip
        tools_zip.tar_gzip(location)

    elif ('bzip2' in filetype):

        import tools_zip
        tools_zip.tar_bzip2(location)

        
    elif ('text' in filetype):
        import tools_txt
        tools_txt.exif(location)
        tools_txt.xxd(location)
        tools_txt.cat(file_location)

    else:
        print('match')


else:
    print("CAUTION:file not found")
