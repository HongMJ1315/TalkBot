import discord
from discord.ext import commands
from disputils import BotEmbedPaginator, BotConfirmation, BotMultipleChoice

def helpset():
  _embed=[]
  _embed.append(discord.Embed(title="The Bot (⁎⁍̴̛ᴗ⁍̴̛⁎)", description="給耍自閉耍邊緣的你 P1", color=0x00ffff)) 
  _embed[0].add_field(name="rb!learn A:B", value="輸入A(可有空格) 回答B(一個關鍵字可以很多回答)\n EX:rb!learn test:test\n The Bot (⁎⁍̴̛ᴗ⁍̴̛⁎)：已學習 test 回復 test", inline=False)
  _embed[0].add_field(name="rb!forget A", value="忘記A的其中一種回答\n EX:rb!forget test\n The Bot (⁎⁍̴̛ᴗ⁍̴̛⁎)：忘記 test", inline=False)
  _embed[0].add_field(name="請注意指令輸入內容",value="後台有紀錄!", inline=False)
  _embed[0].set_footer(text="Made By Mr_JB IG@__mr.jb__")

  _embed.append(discord.Embed(title="The Bot (⁎⁍̴̛ᴗ⁍̴̛⁎)", description="給耍自閉耍邊緣的你 P2", color=0x00ffff)) 
  _embed[1].add_field(name="rb!now", value="取得今年已過%數", inline=False)
  _embed[1].add_field(name="rb!sug A", value="A請取代為建議內容 提供建議\n EX:rb!sug 建議測試\n 已傳送建議：建議測試 給機器人", inline=False)
  _embed[1].add_field(name="rb!TriFun", value="三角函數(sin cos tan)(支援度數及弧度)及反三角函數(asin acos atan)\n EX:rb!learn cos 60°\n The Bot (⁎⁍̴̛ᴗ⁍̴̛⁎)：0.5\n EX:rb!learn cos 1\n The Bot (⁎⁍̴̛ᴗ⁍̴̛⁎)：0.5403\n EX:rb!learn acos 0.5\n The Bot (⁎⁍̴̛ᴗ⁍̴̛⁎)：60°", inline=False)
  _embed[1].add_field(name="請注意指令輸入內容",value="後台有紀錄!", inline=False)
  _embed[1].set_footer(text="Made By Mr_JB IG@__mr.jb__")
  
  _embed.append(discord.Embed(title="The Bot (⁎⁍̴̛ᴗ⁍̴̛⁎)", description="給耍自閉耍邊緣的你 P3", color=0x00ffff)) 
  #_embed[2].add_field(name="rb!plearn A B", value="圖片學習 \n A請輸入ok或start start開始學習 ok結束學習 B為關鍵字\n EX:rb!plearn start test\n The Bot (⁎⁍̴̛ᴗ⁍̴̛⁎)：正在聆聽 test 的回答\n #開始傳圖片\n EX:rb!plearn ok test\n The Bot (⁎⁍̴̛ᴗ⁍̴̛⁎)：關鍵字 test 的回答聆聽完畢", inline=False)
  _embed[2].add_field(name="rb!changelog", value="更新紀錄", inline=False)
  _embed[2].add_field(name="rb!help", value="使用方式", inline=False)
  _embed[2].add_field(name="請注意指令輸入內容",value="後台有紀錄!", inline=False)
  _embed[2].set_footer(text="Made By Mr_JB IG@__mr.jb__")
  return _embed
