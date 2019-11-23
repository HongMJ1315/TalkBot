#!/usr/bin/env python
# coding: utf-8

# In[3]:


import discord
import random
import json
from discord.ext import commands


# In[4]:


bot = commands.Bot(command_prefix='tb!')
_talk={}


# In[5]:


with open('talk.json', 'r') as f:
    talk = json.load(fp=f)
    _talk=talk
    print(talk)


# In[6]:


def keep( ):
    print(talk)
    talkjs = json.dumps(talk)
    fileObject = open('talk.json', 'w')
    fileObject.write(talkjs)
    fileObject.close()


# In[7]:


def _learn(key,val):
    if(not key in _talk):
        _talk[key]=[]
    _talk[key].append(val)
    print(_talk[key])
    keep()
    return("已學習",key,val)


# In[8]:


def _forget(key):
    if(not key in _talk or len(_talk[key])==0):
        return(key,"尚未被學習")
    tmp=random.randint(0,len(_talk[key])-1)
    tmpch=_talk[key][tmp]
    _talk[key].remove(_talk[key][tmp])
    keep()
    return(tmpch,"已被忘記")


# In[9]:


def _add(a,b):
	return (a+b)


# In[10]:


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


# In[11]:


@bot.command()
async def add(ctx, a: int, b: int):
    await ctx.send(_add(a,b))


# In[12]:


@bot.command()
async def learn(ctx, *a):
    b =' '.join(a)
    cut_str=b.split(" ", 1)
    if(len(cut_str)<2):
        await ctx.send("學習格式錯誤")
        return
    await ctx.send(_learn(cut_str[0],cut_str[1]))


# In[13]:


@bot.command()
async def forget(ctx, *a):
    b =' '.join(a)
    if(len(b)<=0):
        await ctx.send("忘記格式錯誤")
        return
    await ctx.send(_forget(b))


# In[14]:


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    key=message.content
    if(key in talk and not talk[key]==[]):
        await message.channel.send(talk[key][random.randint(0,len(talk[key])-1)])
    await bot.process_commands(message)


# In[16]:


bot.remove_command('help')


# In[17]:


@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Mr_JB Talk Bot", description="給耍自閉耍邊緣的你", color=0xeee657)

    embed.add_field(name="tb!learn stringA stringB", value="輸入A 回答B(一個關鍵字可以很多回答)", inline=False)
    embed.add_field(name="tb!forget stringA", value="忘記A的其中一種回答", inline=False)
    embed.add_field(name="tb!help", value="使用方式", inline=False)

    await ctx.send(embed=embed)


# In[18]:


bot.run('NjQ3NDUwMTIzMjUyNjYyMzAz.XdjGCw.Gd8pJaULLWrkHrpaAQZ6-fR4fx0')


# In[ ]:





# In[ ]:




