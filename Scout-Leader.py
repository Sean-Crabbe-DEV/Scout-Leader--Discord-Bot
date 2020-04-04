import os
import time
import discord
from discord.utils import get
from discord.ext import commands

client = discord.Client()
client = commands.Bot(command_prefix = '!')
players = {}

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Plague Inc in Area 51'))
    print('Bot is online!')

############################################ Commands
    
################### Say
@client.command()
@commands.has_permissions(administrator=True)
async def say(ctx, *, msg):
    await ctx.message.delete()
    await ctx.send("{}" .format(msg))
    
################### Ping
@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! The ping is {round(client.latency * 1000, 2)}ms')
    
################### Kick
@client.command()
@commands.has_permissions(administrator=True)
async def kick(ctx, member : discord.Member,*, reason=None):
    await member.kick(reason=reason)

################### Ban    
@client.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, member : discord.Member,*, reason=None):
    await member.ban(reason=reason)

############################################ 

client.run('###Token Here###')
