
import os
import discord
from decouple import config
from discord.ext import commands
import asyncio


intents = discord.Intents.default()
intents.members = True

#Instantiating discord client with prefix
client = commands.Bot(command_prefix = '.', intents=intents)

client.remove_command("help")

#load cogs
@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'Loaded {extension} category!')

#unload cogs
@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send(f'Unloaded {extension} category!')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


#On ready event to set status
@client.event
async def on_ready():
    print('ready!')
    print(f'{client.user} is online!')
    print(f"With the ID {client.user.id}")





#Fetching environment variables
DISCORD_TOKEN = config('DISCORD_TOKEN') 

client.run(DISCORD_TOKEN) 
