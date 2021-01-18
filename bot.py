import os
import discord
import random
import asyncio
import aiohttp
import json
from discord import Game
from discord.ext.commands import Bot
from dotenv import load_dotenv
import asyncpg

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
BOT_PREFIX = ("ht!", "heyTom! ")

client = Bot(command_prefix=BOT_PREFIX)

async def run():
    description = "A bot written in Python that uses asyncpg to connect to a postgreSQL database."

    # NOTE: 127.0.0.1 is the loopback address. If your db is running on the same machine as the code, this address will work
    credentials = {"user": "dev", "password": "watermark11", "database": "devTomBot", "host": "127.0.0.1"}
    db = await asyncpg.create_pool(**credentials)

    # Example create table code, you'll probably change it to suit you
    await db.execute("CREATE TABLE IF NOT EXISTS users(id bigint PRIMARY KEY, data text);")

    bot = Bot(description=description, db=db)
    try:
        await bot.start(config.token)
    except KeyboardInterrupt:
        await db.close()
        await bot.logout()

async def tomHi()
	tomHello = [
		"Heya!"
		"Hey there!"
		"Hey! How's it going?"
		]
	tomGreetChoice = random.choice(tomHello)
	await message.channel.send(tomGreetChoice + message.author.mention)
	return

@client.event
async def on_message(message):
#Check if message is from this bot, ignore if so
	if message.author == client.user:
		return
	raw = message.content
	msg = raw.casefold()
#Determine response based on who is said as best.
	if "tom is the best" in msg or "tom is best" in msg:
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
	elif "ness is the best" in msg or "ness is best" in msg:
		nessBestResp = [
			"You really think so? Eh, alright.",
			"Yeah, he's okay.",
			"I mean, he's not as cool as a certain AI I know, but... Sure."
			]
		nessBestRChoice = random.choice(nessBestResp)
		await message.channel.send(nessBestRChoice)
		return
	elif "preck is the best" in msg or "preck is best" in msg:
		preckBestResp = [
			"You really think so? Eh, alright.",
			"Yeah, he's okay.",
			"I mean, he's not as cool as a certain AI I know, but... Sure."
			]
		preckBestRChoice = random.choice(preckBestResp)
		await message.channel.send(preckBestRChoice)
		return
	elif "robin is the best" in msg or "robin is best" in msg or "rbin is the best" in msg or "rbin is best" in msg:
		RobinBestResp = [
			"I know, right?",
			"Hey! Keep your bits off my lady, pal!",
			"That's an understatement! Unfortunately, I don't know a word that means 'better than the best,' but if I did I'd use it for Robin!"
			]
		RobinBestRChoice = random.choice(RobinBestResp)
		await message.channel.send(RobinBestRChoice)
		return
	elif "cornelius is the best" in msg or "cornelius is best" in msg:
		CorneliusBestResp = [
			"No. Just no.",
			"Oh my robot God, another Ness...",
			"You gotta be kidding! Compared to me?!"
			]
		CorneliusBestRChoice = random.choice(CorneliusBestResp)
		await message.channel.send(CorneliusBestRChoice)
		return


#Begin Other Tom-Specific command section
	elif "Hey Tom, how are you" in msg:
		moodChoice = random.choice(list(open('tomMood.txt')))
		await message.channel.send(moodChoice)
		#await message.channel.send("read ya on mood")
		return
	elif "hey tom" in msg:
		tomHi()
		return
	elif "hi tom" in msg:
		tomHi()
		return
	elif "hey there tom" in msg:
		tomHi()
		return

#message.content.(contains?)("Tom", "tom") AND
#message.content.(contains?)("bodies", "actors")
#ask about commands


#client.loop.create_task(list_servers())
client.run(TOKEN)
