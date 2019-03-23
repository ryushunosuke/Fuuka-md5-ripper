import urllib.request
import urllib.parse
import urllib.error
import urllib.response
import os, sys

if len(sys.argv) != 3:
	print("Invalid arguments have been passed.\nUse with <filename> <page number>\nExiting...")
else:
	output = open(sys.argv[1] + " MD5s.txt",'w')
	string = "#STARTMD5 list of "+sys.argv[1] + "\n"
	fname = sys.argv[1]
	search = "data-md5=\""
	for x in range(int(sys.argv[2])):
		print("On page: " + str(x+1))
		sys.argv[1] = "https://desuarchive.org/a/" + fname + "/page/" + str(x) +'/'
		ourURL = urllib.request.urlopen(sys.argv[1])
		beg = 0
		for line in ourURL.readlines():
			line = line.decode("ascii","ignore")

			#if line.find("title=\"") !=-1:
			#	filename = line[line.find("title=\"")+7:line.find("\"",line.find("title=\"")+8)]
			
			index = line.find(search,beg)
			while line.find(search,beg) !=-1:
				start = line.rfind("\"",0,index+len(search))
				end = line.find("\"",start+1)
				md5 = line[start+1:end]
				if string.find(md5) == -1:
					#Filename does not yet work
					#string += "#filename " + filename + '\n'
					string += "/" + line[start+1:end] + "/" + "\n"
				beg = index + 1
				index = line.find(search,beg)
	
	string += "#ENDMD5 list of " + fname
	output.write(string)