# This is a Discord bot

import discord  # Discord.py library, check the documentation
from discord.ext import commands  # We use this somewhere
import logging  # We also use this
from dotenv import load_dotenv # process the dotfile things
import os  # OS to access the dotfiles i think

# Access stuff in the dotfiles
load_dotenv()
token = os.getenv("DISCORD_TOKEN")

# Configure bot intents
handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w")
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

# Create the bot
bot = commands.Bot(command_prefix="!", intents=intents)

secret_role = "Gamer"

# List of bad words
bad_words = ["shit", "fuck", "nigga", "beat it"]
# Check if bot is active
@bot.event
async def on_ready():
    print(f"We are ready to go in {bot.user.name}")

# Checks for new member that joins the server
@bot.event
async def on_member_join(member):
    await member.send(f"Welcome to the server {member.name}")

# Handles the messages and the bad words
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    for word in bad_words:
        if word in message.content.lower():
            await message.delete()
            await message.channel.send(f"{message.author.mention} -  please dont use that word")

    # I dont know what this line does but please leave this at the end of this function
    await bot.process_commands(message)

# !hello
@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello {ctx.author.mention}!")

@bot.command()
async def assign(ctx):
    role = discord.utils.get(ctx.guild.roles, name=secret_role)
    if role:
        await ctx.author.add_roles(role)
        await ctx.sent(f"{ctx.author.mention} is not assigned to {secret_role}")
    else:
        await ctx.sent(f"Role doesnt exist")

# Run the bot
bot.run(token, log_handler=handler, log_level=logging.DEBUG)
