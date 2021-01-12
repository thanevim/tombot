import os
import random
import asyncio
import aiohttp
import json
from discord import Game
from discrod.ext.commands import Bot
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
BOT_PREFIX = ("ht! ", "heyTom! ")

client = Bot(command_prefix=BOT_PREFIX)

@client.command(name='mood',
	description="Returns the mood of TomBot!",
	pass_context=True)
async def mood(context):
	possible_responses = [
		'Alright! Yourself?',
		'Eh, I could be better!'
		'Now is not a great time...'
	]
	await client.say(random.choice(possible_responses) + ", " + context.message.author.mention)
	
	
	
	
client.loop.create_task(list_servers())
client.run(TOKEN)