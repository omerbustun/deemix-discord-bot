import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():	
	
	guild_count = 0
	for guild in bot.guilds:		
		print(f"- {guild.id} (name: {guild.name})")
		guild_count = guild_count + 1
	print("SampleDiscordBot is in " + str(guild_count) + " guilds.")

@bot.command()
async def test(ctx, arg):
    pass


bot.run("Token")