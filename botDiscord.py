import discord
from discord.ext import commands
import os, binascii
import nginxURLGen

bot = commands.Bot(command_prefix='.')
bot.remove_command('help')

printerName = ["hades", "h", "kraken", "k", "poseidon", "p"]
passwd = ["hacklab!", "Hacklab!", "hacklab!"]
ip = ["216", "217", "218"]

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name="as the world collapsed"))
    
    print('Logged in as', bot.user.name, '(ID:', bot.user.id, ')')
    print('---------------------------------------------------------')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Try '.access [name of printer]'")
    
    else:
        await ctx.send("Something isn't right... `" + error + "`")

@bot.command()
async def access(ctx, printer = None):
    if printer == None:
        await ctx.send("Maybe try to specify a printer `hades, kraken, or poseidon`")
        return
    
    i = 0
    sizeofList = len(printerName)
    while i < sizeofList:
        if printer.lower() == printerName[i]:
            author = ctx.message.author
            token = binascii.b2a_hex(os.urandom(15)).decode("utf-8")
            o=i//2
            
            nginxURLGen.createConf(printerName[o*2], token, ip[o]);
            message = f"{ctx.message.author.mention}, You could access {printerName[o*2].title()} with `hacklab`:`{passwd[o]}` at: https://{printerName[o*2]}.dynamic.hacklabmikkeli.fi/{token}"
            
            await ctx.send(message)
            await author.send(message)
            break
        
        elif sizeofList - i == 1:
            await ctx.send("Printer not found. Try `hades, kraken, or poseidon`")
        
        i += 1

@access.error
async def access_error(ctx, error):
    await ctx.send("Something isn't right... `" + error + "`")

