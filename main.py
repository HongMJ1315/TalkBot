import discord
import random
from discord.ext import commands
import mod.talk.talk
import mod.wlog 
import mod.config
import mod.Tri
import mod.time_per
import mod.sug
import mod.ptalk.forget
import mod.ptalk.config
import mod.sethelp
import keep_alive
from disputils import BotEmbedPaginator, BotConfirmation, BotMultipleChoice



bot = commands.Bot(command_prefix=mod.config.head_key)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

#%數
@bot.command()
async def now(ctx):
    await ctx.send(mod.time_per._time())

#三角函數
@bot.command()
async def TriFun(ctx,*a):
    await ctx.send(mod.Tri._TriFun(a))

#建議
@bot.command()
async def sug(ctx, *a):
    b =' '.join(a)
    if(len(b)==0):
      await ctx.send("建議內容為空")
      return
    await ctx.send(mod.sug._sug(b))
	
#文字學習
@bot.command()
async def learn(ctx, *a):
    b =' '.join(a)
    cut_str=b.split(":", 1)
    if(len(cut_str)<2):
        await ctx.send("學習格式錯誤")
        return
    await ctx.send(mod.talk.talk._learn(cut_str[0],cut_str[1]))

@bot.command()
async def forget(ctx, *a):
    b =' '.join(a)
    if(len(b)<=0):
        await ctx.send("忘記格式錯誤")
        return
    await ctx.send(mod.talk.talk._forget(b))

#圖片學習
'''@bot.command()
async def plearn(ctx,switch,*key):
  key =' '.join(key)
  if(not key in mod.ptalk.config._ptalk):
    mod.ptalk.config._ptalk[key]=[]
  if(switch=='start'):
    mod.ptalk.config.nowlearn[ctx.channel.id]=True
    mod.ptalk.config.nowkey[ctx.channel.id]=key
    await ctx.send("正在聆聽關鍵字"+key+"的回答")
  elif(switch=='ok'):
    mod.ptalk.config.nowlearn[ctx.channel.id]=False
    del mod.ptalk.config.nowkey[ctx.channel.id]
    await ctx.send("關鍵字"+key+"的回答聆聽完畢")'''

'''@bot.command()
async def pforget(ctx, *a):
    b =' '.join(a)
    if(len(b)<=0):
        await ctx.send("忘記格式錯誤")
        return
    await ctx.send(mod.ptalk.forget._pforget(b))'''

#關鍵字
@bot.event
async def on_message(message):
	if(message.author.bot):
		return
	key=message.content
	pot=random.randint(0,1)
	if(pot): #pot=1 send text
		if(key in mod.talk.talk._talk and not mod.talk.talk._talk[key]==[]):
			tmp=random.randint(0,len(mod.talk.talk._talk[key])-1)
			await message.channel.send(mod.talk.talk._talk[key][tmp])
		elif(key in mod.ptalk.config._ptalk and not mod.ptalk.config._ptalk[key]==[]):
			tmp=random.randint(0,len(mod.ptalk.config._ptalk[key])-1)
			await message.channel.send(file=discord.File("mod/ptalk/_IMG/"+mod.ptalk.config._ptalk[key][tmp]))
	else: #pot=0 send text
		if(key in mod.ptalk.config._ptalk and not mod.ptalk.config._ptalk[key]==[]):
			tmp=random.randint(0,len(mod.ptalk.config._ptalk[key])-1)
			await message.channel.send(file=discord.File("mod/ptalk/_IMG/"+mod.ptalk.config._ptalk[key][tmp]))
		elif(key in mod.talk.talk._talk and not mod.talk.talk._talk[key]==[]):
			tmp=random.randint(0,len(mod.talk.talk._talk[key])-1)
			await message.channel.send(mod.talk.talk._talk[key][tmp])

	if(not len(message.attachments)==0):#嘗試尋找圖片
		ptype=message.attachments[0].filename.split(".", 1) #設定副檔名
		if(mod.ptalk.config.nowlearn[message.channel.id]):#圖片學習狀態為ture 執行下四行
			print(mod.ptalk.config.nowkey[message.channel.id],"新增",str(mod.ptalk.config.pcount)+"."+ptype[1])
			mod.ptalk.config._ptalk[mod.ptalk.config.nowkey[message.channel.id]].append(str(mod.ptalk.config.pcount)+"."+ptype[1]) #新增檔案名稱至_ptalk
			await message.attachments[0].save(f'mod/ptalk/_IMG/{str(mod.ptalk.config.pcount)+"."+ptype[1]}') #儲存檔案至/a
			mod.wlog.wlogs(mod.ptalk.config.nowkey[message.channel.id]+"新增"+str(mod.ptalk.config.pcount)+"."+ptype[1])
			await message.channel.send("讀取完畢")
			mod.ptalk.config.pcount+=1
			mod.ptalk.config.keep()
	
	if(key[:3]=='rb!'):
		mod.wlog.wlogs('["'+str(message.author.name)+'" ID :'+str(message.author.id)+']在 server：["'+str(message.guild.name)+'" ID :'+str(message.guild.id)+']執行: " '+key+' "\n')
		await bot.process_commands(message)

bot.remove_command('help')

@bot.command()
async def changelog(ctx):
	embed = discord.Embed(title="更新紀錄", description="", color=0x00ffff)
	embed.add_field(name="The Bot (⁎⁍̴̛ᴗ⁍̴̛⁎) v1.0", value="11/23 原名稱Mr_JB's Talk Bot正式啟用", inline=False)
	embed.add_field(name="The Bot (⁎⁍̴̛ᴗ⁍̴̛⁎) v1.1", value="11/24 更改輸入方式tb!learn A:B", inline=False)
	embed.add_field(name="The Bot (⁎⁍̴̛ᴗ⁍̴̛⁎) v1.1.1", value="11/25 更改指令開頭rb!", inline=False)
	embed.add_field(name="The Bot (⁎⁍̴̛ᴗ⁍̴̛⁎) v1.2", value="11/30 增加指令rb!now", inline=False)
	embed.add_field(name="The Bot (⁎⁍̴̛ᴗ⁍̴̛⁎) v1.3", value="12/01 增加指令rb!sug rb!changelog", inline=False)
	embed.add_field(name="The Bot (⁎⁍̴̛ᴗ⁍̴̛⁎)不重要小更新", value="12/07 改名The Bot (⁎⁍̴̛ᴗ⁍̴̛⁎)", inline=False)
	embed.add_field(name="The Bot (⁎⁍̴̛ᴗ⁍̴̛⁎) v1.4", value="12/09 增加三角函數指令及反三角函數", inline=False)
	embed.add_field(name="The Bot (⁎⁍̴̛ᴗ⁍̴̛⁎) v1.5", value="12/19 圖片學習", inline=False)
	embed.add_field(name="The Bot (⁎⁍̴̛ᴗ⁍̴̛⁎) v1.5.1", value="12/20 改良rb!help指令", inline=False)
	embed.add_field(name="The Bot (⁎⁍̴̛ᴗ⁍̴̛⁎) v1.5.2", value="12/22 暫時移除圖片學習所有功能", inline=False)
	await ctx.send(embed=embed)

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="公告", description="", color=0xff0000)
    embed.add_field(name="修改項目：圖片學習", value="圖片學習功能因伺服器問題暫時移除", inline=False)
    embeds = mod.sethelp.helpset()
    paginator = BotEmbedPaginator(ctx, embeds)
    await ctx.send(embed=embed)
    await paginator.run()

bot.run(mod.config.token)


