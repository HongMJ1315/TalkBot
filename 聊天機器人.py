
import random

talk={}

def learn(key,val):
    if(not key in talk):
        talk[key]=[]
    print("已學習",key,val,end="\n\n")
    talk[key].append(val)

def forget(key):
    if(not key in talk or len(talk[key])==0):
        print(key,"尚未被學習",end="\n\n")
        return
    tmp=random.randint(0,len(talk[key])-1)
    print(talk[key][tmp],"已被忘記",end="\n\n")
    talk[key].remove(talk[key][tmp])

def htu():
    print("歡迎使用Python聊天機器人\n聊天機器人使用格式如下\n學習 (關鍵字) (輸出)\n忘記 (關鍵字)\n呼叫使用說明請輸入(機器人)\n洗版請輸入(洗版)\n輸入時不要加括號",end="\n\n")

def wash():
    for i in range(1000):
        print()

def main(a):
    cut_str=a.split(" ", 2)
    if(cut_str[0]=="學習"):
        if(len(cut_str)<3):
            print("學習格式錯誤",end="\n\n")
            return
        learn(cut_str[1],cut_str[2])
    elif(cut_str[0]=="忘記"):
        if(len(cut_str)<2):
            print("忘記格式錯誤",end="\n\n")
            return
        forget(cut_str[1])
    elif(cut_str[0]=="機器人"):
        htu()
    elif(cut_str[0]=="洗版"):
        wash()
    elif(cut_str[0] in talk and not talk[cut_str[0]]==[]):
        print(talk[a][random.randint(0,len(talk[a])-1)],end="\n\n")
    else:
        print(cut_str[0],"尚未被學習",end="\n\n")
def start():
    htu()
    try:
        while True:
            a=input()
            main(a)
    except EOFError:
        pass
start()
