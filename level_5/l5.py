#Chnage to same directory as file.pickle 
#file.pickle is pasted with the data obtained at url='http://www.pythonchallenge.com/pc/def/banner.p'
#the data at url is already pickeled so, we need to unpickle it


import pickle
import requests

res=requests.get('http://www.pythonchallenge.com/pc/def/banner.p')
filep=open('file.pickle','w') #Just text because data is already pickled
filep.write(res.text)
filep.close()

#Now unpoickle the contents of file with pickle.load()

with open('file.pickle','rb') as f:
    data=pickle.load(f)

print data #Biggerish lists 

#key is to print the symbols with corresponding counts 

for each in data:
	print ''.join(c*n for c,n in each)



