# TO INVITE DE BOT
#https://discordapp.com/oauth2/authorize?client_id=779017802396467220&scope=bot&permissions=0

import discord

# Take token from token file, just for security! :)
def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()

token = read_token()



client = discord.Client()

@client.event
async def on_message(message):
    if message.content.find("!nazi") == 0:
        await message.channel.send("Hi Hitler")


client.run(token)
