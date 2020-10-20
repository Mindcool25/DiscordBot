from random import *
import discord
from discord.ext import commands
from datetime import datetime as d

quotefile = open("cogs/quotes.txt","r")
quotestr = quotefile.read()
quotelist = quotestr.split(' endquote*')
print(quotelist)

class BasicCog(commands.Cog):
		def __init__(self, bot):
				self.bot = bot

		@commands.command(
				name="ping",
				description="Check bot speed and connection",
				aliases=['p'])
		async def ping_command(self, ctx):
				start = d.timestamp(d.now())
				print("Pinging...")
				msg = await ctx.send(content='Pinging')
				await msg.edit(
						content=
						f'Pong!\nOne message round-trip took {( d.timestamp( d.now() ) - start ) * 1000 }ms.'
				)

		@commands.command(
				name="quote",
				description="Get a random quote from the wonderful group of friends.",
				aliases=['q'])
		async def quote_command(self, ctx):
				quotes = quotelist
				quote = quotes[randint(0, len(quotes) - 1)]
				print(f"Sending quote {quote}...")
				msg = await ctx.send(content=quote)
				return

		@commands.command(
				name='oi',
				description='Oi mate get over here!',
				usage='.oi <number of ois>')
		async def oi_command(self, ctx):
				msg = ctx.message.content
				prefix_used = ctx.prefix
				alias_used = ctx.invoked_with
				ois = msg[len(prefix_used) + len(alias_used):]
				print(f"Attempting to send oi {ois} times...")
				if int(ois) < 101:
						for x in range(int(ois)):
								msg = await ctx.send('oi')
				return


def setup(bot):
		bot.add_cog(BasicCog(bot))
