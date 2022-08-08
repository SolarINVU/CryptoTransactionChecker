from calendar import c
from turtle import position
import discord 
from discord.ext import commands
import subprocess
import threading
import aiofiles
import discord
import asyncio
import aiohttp
import random
import ctypes
import re
import os
from discord import Embed
from lxml import html
import requests

ctypes.windll.kernel32.SetConsoleTitleW('CC')
#Depend on your prefix i Used ! for my own <3
prefix = '!'
intents = discord.Intents().all()
bot = commands.Bot(command_prefix=prefix, case_insensitive=True, intents=intents)

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity= discord.Game('Watch and Check Your Addy'))
    print('Bot is Online')

verification_channel = 1004786076747047022

@bot.command()
async def status(ctx, transaction_hash):
    print(f'{ctx.author} | {ctx.author.id} -> #status {transaction_hash}')
    if ctx.channel.type != discord.ChannelType.private:
        if ctx.channel.id == verification_channel:
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(f'https://mempool.space/api/tx/{transaction_hash}/status') as r:
                        r = await r.json()
                        confirmed = r['confirmed']
                    if confirmed == True:
                        embed = discord.Embed(color=16379747, description='Confirmed: ✅')
                        await ctx.send(embed=embed)
                    elif confirmed == False:
                        embed = discord.Embed(color=16379747, description='Confirmed: ❌')
                        await ctx.send(embed=embed)
                    else:
                        raise Exception
            except:
                embed = discord.Embed(color=16379747, description='An error has occured while attempting to run this command!')
                await ctx.send(embed=embed)
        else:
            await ctx.message.delete()

@bot.command()
async def watch(ctx, transaction_hash):
    print(f'{ctx.author} | {ctx.author.id} -> #watch {transaction_hash}')
    if ctx.channel.type != discord.ChannelType.private:
        if ctx.channel.id == verification_channel:
            try:
                embed = discord.Embed(color=16379747, description='I will notify you when this transaction has reached 1 confirmation!')
                await ctx.send(embed=embed)
                async with aiohttp.ClientSession() as session:
                    while True:
                        async with session.get(f'https://mempool.space/api/tx/{transaction_hash}/status') as r:
                            r = await r.json()
                            confirmed = r['confirmed']
                            if confirmed == True:
                                embed = discord.Embed(color=16379747, description=f'`{transaction_hash}` has reached 1 confirmation!')
                                await ctx.author.send(embed=embed)
                                break
                        await asyncio.sleep(60)
            except:
                embed = discord.Embed(color=16379747, description='An error has occured while attempting to run this command!')
                await ctx.send(embed=embed)
        else:
            await ctx.message.delete()




bot.run("")

#Made by SolarINVU With Love <3 