import os
import random
import asyncio
import aiohttp
import json
from discord import Game
from discord.ext.commands import Bot
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
BOT_PREFIX = ("ht! ", "heyTom! ")

client = Bot(command_prefix=BOT_PREFIX)

@client.event
async def on_message(message):
	if message.author == client.user:
		return
	
	if message.content.startswith("Tom is the best!"):
		compResp = [
			"Gee, thanks!!",
			"Aww, you're pretty neat, too, {}!".format(message.author.mention),
			"Hey thanks!",
			"Y'know you're not so bad yourself, {}!".format(message.author.mention),
			"D'aww, you're gonna make me blush! ...oh, wait, I can't."
		]
		complimentChoice = random.choice(compResp)
		await message.channel.send(complimentChoice)
		return

#@client.event
#async def on_message(message):
#	if message.author == client.user:
#		return
	
	if message.content.startswith("Hey Tom how are you"):
		moodChoice = random.choice(list(open('tomMood.txt')))
		await message.channel.send(moodChoice)
		#await message.channel.send("read ya on mood")
		return
	if message.content.startswith("Ness is the best", "Ness is better", "ness is best", "ness is better"):
		nessBestResp = [
			"You really think so? Eh, alright.",
			"Yeah, he's okay.",
			"I mean, he's not as cool as a certain AI I know, but... Sure."
		]
		nessBestRChoice = random.choice(nessBestResp)
		await message.channel.send(nessBestRChoice)
		return
	if message.content.startswith("Preck is the best", "Preck is better", "preck is best", "preck is better"):
		preckBestResp = [
			"You really think so? Eh, alright.",
			"Yeah, he's okay.",
			"I mean, he's not as cool as a certain AI I know, but... Sure."
		]
		preckBestRChoice = random.choice(preckBestResp)
		await message.channel.send(preckBestRChoice)
		return


#message.content.(contains?)("Tom", "tom") AND	
#message.content.(contains?)("bodies", "actors")

	
#client.loop.create_task(list_servers())
client.run(TOKEN)