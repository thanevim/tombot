import os
import discord
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
#Check if message is from this bot, ignore if so
	if message.author == client.user:
		return
	raw = message.content
	msg = raw.casefold()
#Function: determine response based on who is said as best.
	def char_is_best(name):
		if name is "tom":
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
		elif name is "ness":
			nessBestResp = [
				"You really think so? Eh, alright.",
				"Yeah, he's okay.",
				"I mean, he's not as cool as a certain AI I know, but... Sure."
				]
			nessBestRChoice = random.choice(nessBestResp)
			await message.channel.send(nessBestRChoice)
		return
		elif name is "preck":
			preckBestResp = [
				"You really think so? Eh, alright.",
				"Yeah, he's okay.",
				"I mean, he's not as cool as a certain AI I know, but... Sure."
				]
			preckBestRChoice = random.choice(preckBestResp)
			await message.channel.send(preckBestRChoice)
			return
#is best event listener
	if "is best" in msg:


#Tom
	if message.content.startswith("Tom is the best"):
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
	elif "tom is the best" in msg:
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
	elif "ness is the best" in msg:
		nessBestResp = [
			"You really think so? Eh, alright.",
			"Yeah, he's okay.",
			"I mean, he's not as cool as a certain AI I know, but... Sure."
			]
		nessBestRChoice = random.choice(nessBestResp)
		await message.channel.send(nessBestRChoice)
		return
	elif message.content.startswith("Preck is the best"):
		preckBestResp = [
			"You really think so? Eh, alright.",
			"Yeah, he's okay.",
			"I mean, he's not as cool as a certain AI I know, but... Sure."
			]
		preckBestRChoice = random.choice(preckBestResp)
		await message.channel.send(preckBestRChoice)
		return
	elif message.content.startswith("Robin is the best"):
		RobinBestResp = [
			"I know, right?",
			"Hey! Keep your bits off my lady, pal!",
			"That's an understatement! Unfortunately, I don't know a word that means 'better than the best,' but if I did I'd use it for Robin!"
			]
		RobinBestRChoice = random.choice(RobinBestResp)
		await message.channel.send(RobinBestRChoice)
		return
	elif message.content.startswith("Cornelius is the best"):
		CorneliusBestResp = [
			"No. Just no.",
			"Oh my robot God, another Ness...",
			"You gotta be kidding! Compared to me?!"
			]
		CorneliusBestRChoice = random.choice(CorneliusBestResp)
		await message.channel.send(CorneliusBestRChoice)
		return


#Begin Other Tom-Specific command section
	elif message.content.startswith("Hey Tom, how are you"):
		moodChoice = random.choice(list(open('tomMood.txt')))
		await message.channel.send(moodChoice)
		#await message.channel.send("read ya on mood")
		return
	elif message.content.contains("Hey Tom"):
		await message.channel.send("Hey! How's it going?")
		return
	elif message.content.contains("Hi Tom"):
		await message.channel.send("Heya!")
		return
	elif message.content.contains("hey tom"):
		await message.channel.send

#message.content.(contains?)("Tom", "tom") AND
#message.content.(contains?)("bodies", "actors")
#ask about commands


#client.loop.create_task(list_servers())
client.run(TOKEN)
