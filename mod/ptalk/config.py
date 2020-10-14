import json


nowlearn={}
_ptalk={}
nowkey={}
pcount=0


with open('ptalk_dic.json', 'r') as f:
	ptalk = json.load(fp=f)
	_ptalk=ptalk
	print(ptalk)

with open('mod/ptalk/pamount.txt') as f:
	pamount = f.read()
	pcount=int(pamount)

def keep( ):
    ptalkjs = json.dumps(_ptalk)
    fileObject = open('ptalk_dic.json', 'w')
    fileObject.write(ptalkjs)
    fileObject.close()
    f = open('mod/ptalk/pamount.txt','w') 
    f.write(str(pcount))    
    f.close()  
	