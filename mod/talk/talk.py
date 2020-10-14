import json
import random
from ..wlog import wlogs
_talk={}

with open('talk_dic.json', 'r') as f:
	talk = json.load(fp=f)
	_talk=talk
	print(talk)

def keep( ):
    talkjs = json.dumps(_talk)
    fileObject = open('talk_dic.json', 'w')
    fileObject.write(talkjs)
    fileObject.close()
	
def _learn(key,val):
	if(not key in _talk):
		_talk[key]=[]
	_talk[key].append(val)
	keep()

	wlogs(key+" 新增 "+val+'\n')
    
	print(key,"新增",val)
	return("已學習 "+key+" 回覆 "+val)

def _forget(key):
	if(not key in _talk or len(_talk[key])==0):
		return(key+"尚未被學習")
	tmp=random.randint(0,len(_talk[key])-1)
	tmpch=_talk[key][tmp]
	_talk[key].remove(_talk[key][tmp])
	keep()
    
	wlogs("關鍵字 "+key+" 回答 "+tmpch+" 已被忘記\n")
    
	print("關鍵字 "+key+" 回答 "+tmpch+" 已被忘記")
	return("關鍵字 "+key+" 回答 "+tmpch+" 已被忘記")