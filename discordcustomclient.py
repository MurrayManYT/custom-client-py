import discord
from discord.ext import commands
from discord.ext.commands import Bot
client = commands.Bot(command_prefix="!")
counter = 0
@client.event
async def on_ready():
    print("bot is ready")
    
    
@client.command()
async def eko (ctx, *, message):
    #await ctx.send(message)
    print (message)
    
'''@client.command()
async def echo(message):
    await message.send(message)'''
    
@client.command()
async def customclientmode(ctx):
    customclient = input("enter stuff here")
    #while customclient == "":
    await ctx.send(customclient)
    while counter == 0:
        customclient = input("")
        await ctx.send(customclient)
    
client.run("token here")
