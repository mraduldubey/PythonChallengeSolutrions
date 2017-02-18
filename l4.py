#Puzzle involves sequencitally linked urls where nothing="" is obtained successively
#Starts from 12345 branches at 82682 into 82683 and 63579: finally ends at the result
import requests
import re

reobj=re.compile(r'(\d+)')
nothing='63579' #Last branch which sets out the answer
count=0

while count<400:
	res=requests.get('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='+nothing)
	mo=reobj.findall(res.text)
	nothing=str(mo[0])
	print nothing
	count+=1
	print count
print nothing


        
