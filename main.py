import discord
from discord.ext import commands


def get_prefix(bot, message):
    # The prefix for bot commands
    prefixes = ["."]

    return commands.when_mentioned_or(*prefixes)(bot, message)


extensions = ['cogs.basic','cogs.suggest','cogs.fun']

bot = commands.Bot(
    command_prefix=get_prefix, description='A bot for general use.')

if __name__ == '__main__':
    for extension in extensions:
        bot.load_extension(extension)



@bot.event
async def on_ready():
    print(
        f'\n\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n'
    )

bot.run('TOKEN', bot=True, reconnect=True)