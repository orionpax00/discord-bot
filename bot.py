import discord
import os

client = discord.Client()


@client.event
async def on_message(message):
		id = client.get_guild(752107621397430385)
		if message.author == client.user:
				return

		if message.content.startswith('geany'):
				await message.channel.send('niralj tu phir aa gaya')
				
		if '<@!679722852311761010>' in message.content.split():
				await message.channel.send('Durgesh is offline sorry!!!!')
		
		if 550034158462828554 == message.author.id:
				await message.channel.send('madarchod tu phir aa gaya')

		if 724625799801471038 == message.author.id:
				await message.channel.send('dekho dekho kon aaye hain...')
				
		if '<@!550034158462828554>' in message.content.split():
				await message.channel.send('ye madarchod hai')

client.run(os.environ['DISCORD_BOT'])

#https://discord.com/oauth2/authorize?client_id=775709662519623711&scope=bot
