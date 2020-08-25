import discord
from discord.ext import commands
from datetime import datetime as d

class MembersCog(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command(
		name="ping",
		description="Check bot speed and connection",
		aliases=['p']
		)
	async def ping_command(self,ctx):
		start = d.timestamp(d.now())
		msg = await ctx.send(content='Pinging')
		await msg.edit(content=f'Pong!\nOne message round-trip took {( d.timestamp( d.now() ) - start ) * 1000 }ms.')
		return
	@commands.command(
		name="quote",
		description="Get a random quote from the wonderful dnd group.",
		aliases=['q']
	)
	async def quote_command():
		return
def setup(bot):
	bot.add_cog(MembersCog(bot))