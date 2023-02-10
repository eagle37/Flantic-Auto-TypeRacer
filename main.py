import os
os.system('pip install discord.py-self')
import discord
from discord.ext import commands
import time
import httpx

client = commands.Bot(command_prefix='!',self_bot=True)

Token = ""

def solver(solution_img_url: str):
        url = 'https://Ocr-api.phantomxnovaxd.repl.co/api/v1/solver'
        data = {'image_url': solution_img_url,"Authorization": Token}
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        r = httpx.post(url, data=data, headers=headers)
        print(r.json())
        return r.json()['text'] , r.json()['time']


@client.event
async def on_message(message: discord.Message):
    if message.author.id == 825617171589759006:

        try:
            if message.embeds[0].image.url:
                time_start = time.time()
                url = message.embeds[0].image.url
                s = solver(url)
                solution = s[0]
                time_taken = time.time() - time_start
                solving_time = s[1]
                await message.reply(s[0])
                await message.reply('Solved! Time taken: ' + str(time_taken) + ' seconds' + ' | Solving time: ' + str(solving_time) + ' seconds')
                print("Solving | " + url)
                print("Solved Image: " + s)
                
            else:
                print("No Image")

        except Exception as e:
            print("Couldnt solve game or wasnt valid")
            print(e)

                

    else:
        pass
        


client.run(Token)
