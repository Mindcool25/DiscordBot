from random import *
import discord
from discord.ext import commands
from datetime import datetime as d


class BasicCog(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command(
		name="ping",
		description="Check bot speed and connection",
		aliases=['p'])
	async def ping_command(self, ctx):
		start = d.timestamp(d.now())
		msg = await ctx.send(content='Pinging')
		await msg.edit(
		content=
		f'Pong!\nOne message round-trip took {( d.timestamp( d.now() ) - start ) * 1000 }ms.')

	@commands.command(
		name="quote",
		description="Get a random quote from the wonderful dnd group.",
		aliases=['q'])
	async def quote_command(self, ctx):
		quotes = (
			'“Sometimes less is think... More”\n-Daniel / @Stik555 ',
			'“It’s sky color”\n-Kyle / @Mastachi ',
			'“Bug sanitizer”\n-Daniel / @Stik555 ',
			'"Spray it in your eyes, thats where it tastes best"\n-Kyle / @Mastachi',
			"Tell us if you are the killer, or don't if your not!\n-Ethan / @BBJPZ",
			'“To be or not to be with a woman”\n-Ethan / @BBJPZ on flirting',
			'“I know just the role play server to stand in front of”\n-Ethan / @W͡҉͞͡à̢͡n̴͝͝d̶̛̛é͡͝r̶͝͡ę̴͘r҉',
			'"You do not have the equipment to slow cook the bear."\n-Daniel / @Stik555',
			'"You just throw corn at him in rage!"\n-Ethan / @W͡҉͞͡à̢͡n̴͝͝d̶̛̛é͡͝r̶͝͡ę̴͘r҉',
			'"*Sexy fire noises*"\n-Daniel / @Stik555',
			'"Go Jebidiah!"\n-Ethan / @W͡҉͞͡à̢͡n̴͝͝d̶̛̛é͡͝r̶͝͡ę̴͘r҉',
			'“I WILL MICROWAVE AT YOU”\n-Daniel/@Stik555',
			'“I am the winner because the box has chosen me!!!!”\n-Daniel / @Stik555',
			'“It was a mutual nonconsensual mauling”\n-Daniel/@Stik555',
			'“#SeeTheChicken #SaveTheChicken”\n-Daniel/@Stik555',
			"'Nah, we'll be fine. And if not...\nWe'll be fine.'\n-Ethan / @W͡҉͞͡à̢͡n̴͝͝d̶̛̛é͡͝r̶͝͡ę̴͘r҉",
			'“There is always a place for innuendos” -Kyle/ @Mastachi',
			'“But Charlie....” -Ethan/ @W͡҉͞͡à̢͡n̴͝͝d̶̛̛é͡͝r̶͝͡ę̴͘r҉',
			'“I was trying to touch your feet but didn’t feel it” \n“Yah I felt that”\n-Ethan and Daniel / @W͡҉͞͡à̢͡n̴͝͝d̶̛̛é͡͝r̶͝͡ę̴͘r҉ @Stik555',
			'“I gotta zoom meeting, so back to the closet”\n-Ethan/ @W͡҉͞͡à̢͡n̴͝͝d̶̛̛é͡͝r̶͝͡ę̴͘r҉',
			'“Do you know how much I want a beer belly and can’t get one”\n-Joseph / @Fuitnugget23',
			'"I don\'t... want to be a prostitute"\n-Maggi / @AndPeggy',
			'"Alliteration sells... beer"\n- Daniel / @Stik555',
			'"gastropod weeness"\n- Daniel / @Stik555',
			'“Farmer Brown’s mushrooms”\n-Kyle / @Mastachi on psychedelics',
			'"You can hear it whisper into your ear, as you hear its wet, plump lips smacking against each other. It blinks, letting out a sickly squelch as its eye lids separate once more."\n-Daniel / @Stik555\n:eye: :lips: :eye:',
			'“Losing a bet is the best excuse for everything”\n-Ethan / @W͡҉͞͡à̢͡n̴͝͝d̶̛̛é͡͝r̶͝͡ę̴͘r҉',
			'“You know what would be a real smart war crime?”\n-Seth / @Owenthegreat',
			'“I wanted to stab him but I had to die!”\n-Ethan / @W͡҉͞͡à̢͡n̴͝͝d̶̛̛é͡͝r̶͝͡ę̴͘r҉',
			'"My favorite 2 characters to mate..."\n-Ethan / @BBJPZ',
			'“Alternatively Wufff!”\n-Ethan/ @W͡҉͞͡à̢͡n̴͝͝d̶̛̛é͡͝r̶͝͡ę̴͘r҉',
			'"What do boys do when they get together? Thigh shaping in sequence ensues"\n-Daniel / @Stik555'
		)
		quote = quotes[randint(0, len(quotes) - 1)]
		msg = await ctx.send(content=quote)
		return
	@commands.command(
				name='oi',
				description='Oi mate get over here!',
				usage='.oi <number of ois>'
			)
	async def oi_command(self, ctx):
		return

def setup(bot):
	bot.add_cog(BasicCog(bot))
