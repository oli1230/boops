import discord
from discord.ext import commands
import music_player
import os

cogs = [music_player]

boops_bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

for cog in cogs:
    cog.setup(boops_bot)

boops_bot.run(os.environ['DISCORD_SERVER_TOKEN']) 