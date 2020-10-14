import mod.wlog

def _sug(line):
    logs=open('suggestion.txt','a')
    logs.writelines(line+'\n')
    logs.close()
    mod.wlogs("新增建議 "+line+'\n')
    return("以傳送建議："+line+"給機器人")