from discord.ext import commands

GUILD_ID = 725343462291144764
SUGGESTIONS_ID = 725361186383724577

class SuggestCog(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command(
		name='suggest',
		description='The command to suggest an idea for the minecraft server',
		aliases=['s']
	)
	async def SuggestCommand(self, ctx, *, s_input: str):
		author = str(ctx.author)
		suggestion = 'suggestion by: '+ author + '\n' + '**' + s_input + '**' + '\nPlease react with :arrow_up: or :arrow_down: to vote'
		print(f"Sent suggestion {suggestion}")
		channel = self.bot.get_channel(725361186383724577)
		msg = await channel.send(suggestion)
		await msg.add_reaction('⬆')
		await msg.add_reaction('⬇')

def setup(bot):
	bot.add_cog(SuggestCog(bot))