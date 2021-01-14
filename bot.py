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
		moodResp = [
		"Alright! Yourself?",
		"Eh, I could be better!",
		"Now is not a great time...",
		"My mood? Hmm... Well, I'm pretty happy, except for when I'm sad, nervous, or upset. But usually happy.",
		"I've been better. Ness won't stop bugging me to join his 'Way of the Cactus' meditations. They're so boring! And that's coming from a guy who spent a couple of centuries on hold with the GHCC!",
		"My mood is moody. Feeling very mood right now. Such mood.",
		"My mood? For the right price, it's whatever you want it to be... Psyche! Haha, as if I were that easy!",
		"I'll be honest, I don't really have 'moods,' I just simulate them for the sake of humans.",
		"You want my mood? You want my mood?! ***YOU CAN'T HANDLE MY MOOD!!***",
		"Hmm, mood... Moooood... Mmmmmooooooooooooooood....../n/nI'm sorry, what was the question again?",
		"#Error: variable \{mood\} not found",
		"I was having a pretty good day until some squishy human decided to ask about my mood.../n/nOh, shoot, you're still here!",
		"*Cut!* Sorry, you're just not selling it. I don't believe you *really* want to know my mood."
		]
		#moodChoice = random.choice(moodResp)
		moodChoice = random.choice(list(open('tomMood.txt')))
		await message.channel.send(moodChoice)
		#await message.channel.send("read ya on mood")
		return


#message.content.(contains?)("Tom", "tom") AND	
#message.content.(contains?)("bodies", "actors")

	
#client.loop.create_task(list_servers())
client.run(TOKEN)