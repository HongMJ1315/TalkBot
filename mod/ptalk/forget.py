
import mod.ptalk.config
import random


def _pforget(key):
    if(not key in mod.ptalk.config._ptalk or len(mod.ptalk.config._ptalk[key])==0):
        return(key+"尚未被學習")
    tmp=random.randint(0,len(mod.ptalk.config._ptalk[key])-1)
    mod.ptalk.config._ptalk[key].remove(mod.ptalk.config._ptalk[key][tmp])
    mod.ptalk.config.keep()

    return("關鍵字 "+key+" 的回答已被忘記")