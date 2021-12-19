import discord
from discord.ext import commands
import nginxURLGen
import os, binascii

printerName = ["hades", "kraken", "poseidon"]
passwd = ["hacklab!", "Hacklab!", "hacklab!"]
ip = ["216", "217", "218"]

bot = commands.Bot(command_prefix='.')
@bot.event
async def on_ready():
    i = 0
    sizeofList = len(printerName)

    embedVar = discord.Embed(title="Hyvää huomenta!", description="Octoprint links had been renewed.", color=0x00ff00)
    while i < sizeofList:
        token = binascii.b2a_hex(os.urandom(15)).decode("utf-8")
        
        nginxURLGen.createConf(printerName[i], token, ip[i]);
        embedVar.add_field(name=printerName[i].title(), value=f"Use `hacklab`:`{passwd[i]}` to access: https://{printerName[i]}.dynamic.hacklabmikkeli.fi/{token}", inline=False)
        
        i += 1

    await channel.send(embed=embedVar)
    await bot.logout()
