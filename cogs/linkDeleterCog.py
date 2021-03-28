import discord
from discord.ext import commands
import asyncio
from main import client


class exampleCog(commands.Cog):
    def __init__(self, client):
        self.client = client




def setup(client):
    client.add_cog(exampleCog(client))
    print("exampleCog LOADED!") 
