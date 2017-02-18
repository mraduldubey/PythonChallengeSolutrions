import zipfile
import os
import re

zipobj=zipfile.ZipFile('channel.zip','r')
zipobj.extractall('channelf') #channelf folder is created in os.getcwd() i.e. current directory

os.chdir('channelf')
 
print os.listdir(os.getcwd()) #shows a readme.txt
content=open('readme.txt','r').read()
print content #welcome to my zipped list.\n\nhint1: start from 90052\nhint2: answer is inside the zip\n'


re_obj=re.compile(r'\d+') #Each file consists of next file's name as the number

next_file=90052 #We get this from readme.txt

comments='' #This must store the comments of all individual files of channel.zip

while True:      
	curr_file=str(next_file)+'.txt'
	content=open(curr_file,'r').read()

	zipinfo_obj=zipobj.getinfo(curr_file) #Returns a ZipInfo type object which has info about indidual files 
	comments+=zipinfo_obj.comment
	mo=re_obj.search(content)  #Returns match object for first occurence of pattern
	next_file=mo.group()
	print comments

#Programs exits with an error 
#The answer is evident 

#Bingo!





