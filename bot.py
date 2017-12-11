import discord
import asyncio
import getpass
import requests



email = input("Enter email\n")
password = getpass.getpass('Enter password\n')

messages_since_started_script = 0

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
    global messages_since_started_script
    if(message.author == client.user):
        if message.content.startswith('!test'):
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
            on = True
            print("Starting bot")
            while on:
                r = requests.get(url = "https://icanhazdadjoke.com/", headers = {'Accept': 'application/json'})
                response = r.json()
                await client.send_message(destination = message.channel, content = response['joke'], tts = True)
                messages_since_started_script += 1
                await asyncio.sleep(60)
        elif message.content.startswith('!pause'):
            print("Pausing bot")
            on = False
        elif message.content.startswith('!status'):
            await client.send_message(message.channel, 'Your naughty ass has sent ' + str(messages_since_started_script) + ' since script started' )
        elif message.server.name == 'LoL Chat':
            print('Checking' + message.content.lower())
            profanityCheck = requests.get(url = 'http://www.purgomalum.com/service/containsprofanity?text=' + message.content.lower())
            if profanityCheck.text == 'true' :
                await client.send_message(destination = message.channel, content = 'Watch your profanity!', tts = True)

client.run(email,password)