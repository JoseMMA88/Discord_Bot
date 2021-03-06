# TO INVITE DE BOT
#https://discordapp.com/oauth2/authorize?client_id=779017802396467220&scope=bot&permissions=0

#id = 779017373952901122 server ID

import discord
import time
import asyncio

# Global variables
client = discord.Client()


# Take token from token file, just for security! :)
def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()

token = read_token()


# Read server id, for import bot to server
def read_server_id():
    with open("token.txt", "r") as i:
        lines = i.readlines()
        return lines[1].strip()


# Read valid users, for bot raid admins
def read_valid_users():
    count = 0
    with open("valid_users.txt", "r") as v:
        return [line.strip() for line in v]

valid_users = read_valid_users()


#API Discord methods implementation
@client.event
async def on_member_join(member):
    for channel in member.server.channels:
        if str(channel) == "general":
            await client.send_message(f"""Welcome to the server {member.mention}""")


@client.event
async def on_message(message):
    id = client.get_guild(int(read_server_id()))
    channels = ["commands"]

    if str(message.channel) in channels and str(message.author) in valid_users:
        if message.content.find("!hi") == 0:
            await message.channel.send("Helloooo")
        elif message.content == "!users":
            await  message.channel.send(f"""# of Members {id.member_count}""")
    else:
        print(f"""User: message.author tried to do command {message.content}, in channel {message.channel}""")



client.run(token)

