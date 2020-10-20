from random import *
import discord
from discord.ext import commands

class FunCog(commands.Cog):
		def __init__(self, bot):
			self.bot = bot

			@commands.command(
				name='roll',
				description='Rolls dice. .roll {number}d{number}',
				aliases=['r']
			)
			async def roll_command(self, ctx, s_inputs):
					dice = 1
					sides = 1
					print(s_inputs)


def setup(bot):
	bot.add_cog(FunCog(bot))