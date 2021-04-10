FILE INSPECTOR.

--------------

INSIGHT:The aim of this project is to extract the data from various file types that we use daily. We extract data from the files we want by presenting its location as input with the help of Linux command line tools.After analysis the output of some tools is written in to an output.txt file from which the further analysis if needed may be performed at will.The output from certain tools which can't be written to a file must be gone through accordingly as stated at respective tools in output.txt.Thid tool demands Linux commnand line interface(terminal) to work.

FILE FORMATS SUPPPORTED:
PNG,JPEG,ZIP,BMP,PDF,TEXT.

The following linux command line tools are used,
1.Exiftool
2.Binwalk
3.strings
4.zsteg
5.foremost
6.6.bulk_extractor
7.hashdeep
8.peepdf
9.pdf_parser
10.pdfid
11.tar
11.1.with flag -xvzf
11.2.with flag -xjvf
12.unzip
13.zidet
14.zipinfo

The python modules that came handy are:

1.os module
2.subprocess module(to run commands/tools)
3.re(regular expression)module
4.concurrent.futures(threading)

REQUIREMENTS:
To use this tool you must have linux and python 3 installed on that machine.

HOW TO USE:
To use this tool after you met the requirements,download the tool
and run: python3 file_identifier_and_executer.py
One will be prompted to enter the exact file location,after doing so the process starts and the output will be written to output.txt(whenever possible).
This will do the job!

Note: The hexdump of your target file can be easily obtained by peforming a simple xxd command with a flag -p .
command: xxd -p file_location.
This will print the output of the command to STDOUT.




