import subprocess
import os
import re
import concurrent.futures

location=input('enter the location of target file:')
if os.path.isfile(location):
    f1=subprocess.run(['file',location],capture_output=True,text=True)
    filetype=re.findall(r'\w+',f1.stdout)

    
    if ('PNG' in filetype):
        import tools_png
        with concurrent.futures.ThreadPoolExecutor() as ex:
            f1=ex.submit(tools_png.exif,location)
            f2=ex.submit(tools_png.bw,location)
            f3=ex.submit(tools_png.strs,location)
            f5=ex.submit(tools_png.zsteg,location)
            f6=ex.submit(tools_png.foremost,location)
            f7=ex.submit(tools_png.bulk_extractor,location)
            f8=ex.submit(tools_png.hashdeep,location)
    elif ('JPEG' in filetype):

        import tools_jpg
        with concurrent.futures.ThreadPoolExecutor() as ex:
            p1=ex.submit(tools_jpg.exif,location)
            p2=ex.submit(tools_jpg.bw,location)
            p3=ex.submit(tools_jpg.strs,location)
            p5=ex.submit(tools_jpg.bulk_extractor,location)
            p6=ex.submit(tools_jpg.hashdeep,location)

    elif ('PDF' in filetype):
        import tools_pdf
        with concurrent.futures.ThreadPoolExecutor() as ex:
            k1=ex.submit(tools_pdf.exif,location)
            k2=ex.submit(tools_pdf.bw,location)
            k3=ex.submit(tools_pdf.strs,location)
            k5=ex.submit(tools_pdf.peepdf,location)
            k6=ex.submit(tools_pdf.bulk_extractor,location)
            k7=ex.submit(tools_pdf.pdf_parser,location)
            k8=ex.submit(tools_pdf.pdfid,location)

    elif ('BMP' in filetype):

        import tools_bmp
        with concurrent.futures.ThreadPoolExecutor() as ex:
            b1=ex.submit(tools_bmp.exif,location)
            b2=ex.submit(tools_bmp.bw,location)
            b3=ex.submit(tools_bmp.strs,location)
            b5=ex.submit(tools_bmp.zsteg,location)
            b6=ex.submit(tools_bmp.hashdeep,location)

    elif ('gzip' in filetype):

        import tools_zip
        with concurrent.futures.ThreadPoolExecutor() as ex:
            t1=ex.submit(tools_zip.tar_gzip,location)

    elif ('bzip2' in filetype):

        import tools_zip
        with concurrent.futures.ThreadPoolExecutor() as ex:
            v1=ex.submit(tools_zip.tar_bzip2,location)
        

    elif ('Zip' in filetype):

        import tools_zip
        with concurrent.futures.ThreadPoolExecutor() as ex:
            z1=ex.submit(tools_zip.zipped,location)
            z2=ex.submit(tools_zip.zipdet,location)
            z3=ex.submit(tools_zip.zipinfo,location)

        
    elif ('text' in filetype):
        import tools_txt
        with concurrent.futures.ThreadPoolExecutor() as ex:
            t1=ex.submit(tools_txt.exif,location)
            t2=ex.submit(tools_txt.xxd,location)
            t3=ex.submit(tools_txt.cat,location)

    else:
        print('file type is not supported')
else:
    print('file  not found')
