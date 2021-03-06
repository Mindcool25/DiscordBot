from random import *
import discord
from discord.ext import commands
from datetime import datetime as d
import json

f = open('cogs/quotes.json')
quotes = json.load(f)

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
				quote, author = choice(list(quotes.items()))
				sending = f"{quote}\n- {author}"

				print(f"Sending quote\n{quote}\n- {author}...")
				msg = await ctx.send(content=sending)
				return

		@commands.command(
			name='quotenum',
			description='Show how many quotes there are.',
			aliases = ['qn']
		)
		async def quotenum_command(self, ctx):
			print(f"Sending quote number... Grand total of {len(quotes)}")
			sent = f"There are {len(quotes)} quotes in quotebot."
			msg = await ctx.send(content=sent)
			return

		@commands.command(
			name='quotestats',
			description='Search for word in all quotes and returns number of times that word appeared.',
			aliases=['qs']
		)
		async def quotestats_command(self, ctx):
			count = 0
			msg = ctx.message.content
			prefix_used = ctx.prefix
			alias_used = ctx.invoked_with
			word = msg[len(prefix_used) + len(alias_used):]
			word = word[1:]
			msg = await ctx.send(content='Searching...')
			for i in quotes:
				if word in i:
					count += 1
				elif word in quotes[i]:
					count +=1
			await msg.edit(content=f"There are {count} instances of '{word}'.")
			print(f"Found {count} instances of '{word}'")
			return

		@commands.command(
			name='quoteincludes',
			description='Search for quotes with a specific word and return a random one from that list',
			aliases=['qi'],
			usage='.qi <search quiry>'
		)
		async def quoteincludes_command(self,ctx):
			msg = ctx.message.content
			prefix_used = ctx.prefix
			alias_used = ctx.invoked_with
			word = msg[len(prefix_used) + len(alias_used):]
			word = word[1:]
			print(f"Searching for {word}...")
			msg = await ctx.send(content='Searching...')
			searchedquotes = []
			for i in quotes:
				if word in i:
					searchedquotes.append([i,quotes[i]])
				elif word in quotes[i]:
					searchedquotes.append([i,quotes[i]])
			print(f"Found {len(searchedquotes)} instances of {word}")
			quote, author = choice(list(searchedquotes))
			sending = f"{quote}\n- {author}"
			print(f"Sending {sending}")
			await msg.edit(content=sending)

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
		
		@commands.command(
			name='github',
			description='Get a link to the github page for bot source code.',
			aliases=['g','code','source']
		)
		async def github_command(self,ctx):
			link = 'link to source code:\nhttps://github.com/Mindcool25/DiscordBot'
			print('Sending link...')
			msg = await ctx.send(content=link)
			return

def setup(bot):
		bot.add_cog(BasicCog(bot))
