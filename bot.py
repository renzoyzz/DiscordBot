import discord
import asyncio
import requests
import getpass

email = input("Enter email\n")
password = getpass.getpass('Enter password\n')

on = True

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    global on
    if message.content.startswith('!count'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'You have {} messages.'.format(counter))
    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')
    elif message.content.startswith('!start'):
        if(message.author == client.user):
            on =True
            print("Starting bot")
            while on:
                r = requests.get(url = "https://icanhazdadjoke.com/", headers = {'Accept': 'application/json'})
                response = r.json()
                await client.send_message(destination = message.channel, content = response['joke'], tts = True)
                await asyncio.sleep(60)
    elif message.content.startswith('!pause'):
        print("Pausing bot")
        on = False

client.run(email,password)