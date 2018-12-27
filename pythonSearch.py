#!/usr/bin/env python

'''
File name: pythonSearch.py
Description: Search file directory for keywords and output line that matches to a file
__author__ = "Robert Morrow"
__copyright__ = "Copyright 2007, The Cogent Project"
__credits__ = ["Robert Morrow"]
__license__ = "MIT"
__version__ = "1.0.1"
__maintainer__ = "Robert Morrow"
__email__ = "woklabs@gmail.com"
__status__ = "Testing"
'''

import time, os

## directory where programs live ##
files_in = "C:\Temp\WorkingCode"

## string to search files in files_in directory ##
searchStr = 'Contact'
print('Searching for (',searchStr,') in directory: ',files_in)

searchStrLower = searchStr.lower()

## directory where the output results are written ##
t = time.localtime()
timestamp = time.strftime('%m-%d-%Y_%H%M%S', t)
files_out = files_in + "\\" + searchStr + "-" + timestamp + ".txt"

## list for allowed files extensions ##
def allowedExt(file):

	list = ['.cs','.txt']
    
	filename, file_extension = os.path.splitext(file)
	if file_extension in list:
		return True
	else:
		return False
    
cnt=0	
list_out = []
tempName = ''
seporator = '=============================================================='

for root, dirs, files in os.walk(files_in,topdown=False):
    
    for file in files:
            
        filepath = root + '\\' + file
        
        ## only search wanted file extensions ##
        if allowedExt(filepath):

            with open(filepath) as search:
                for line in search:
                    line = line.rstrip()
                    if searchStrLower in line.lower():
                        cnt+=1
                        if not tempName==file:
                            list_out.append(seporator)
                        list_out.append(filepath + '  ===>>>' + line)
                        tempName = file

for item in list_out:
    with open(files_out,'a') as f:
        f.write(item + '\n')

print('Wrote',cnt,'lines out to:',files_out)
