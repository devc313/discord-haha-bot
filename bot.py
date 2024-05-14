import discord
from discord.ext import commands

TOKEN = 'your bot token'

intents = discord.Intents.default()
intents.reactions = True
intents.messages = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user.name} haha atmaya hazir')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    await message.add_reaction('<:haha:1031174030478278748>')

    await bot.process_commands(message)

bot.run(TOKEN)
