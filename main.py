import discord
import generator
import progress
import os

client = discord.Client(intents=discord.Intents.all())



@client.event 
async def on_ready(): 
    print("Bot is online")

@client.event
async def on_message(message): 
    print(message.content)
    if message.author == client.user: 
        return
    else: 
        if "!generate" in message.content:
          async with message.channel.typing():
              await message.reply(f"Andrew Tate has been banned from {generator.randomizeBrands()} {generator.randomizeDescriptors()} {generator.randomizeItems()} {generator.randomizeSuffix()}due to {generator.randomizeReason()}")
        else: 
          if "!multiple" in message.content:
              curString = ""
              raw = message.content
              current = 0 
              max = int(raw.split(" ")[1])
              statMsg = await message.reply(f"Starting...")
              while current < max: 
                async with message.channel.typing():
                  curString = curString + f"Andrew Tate has been banned from {generator.randomizeBrands()} {generator.randomizeDescriptors()} {generator.randomizeItems()} {generator.randomizeSuffix()}due to {generator.randomizeReason()}\n"
                  await statMsg.edit(content=f"Generating... { int((current / max) * 100) }%\n ``{progress.getProgressBar(int((current / max) * 100))}``")
                  current += 1 

              try: 
                await statMsg.delete()
                await message.reply(curString)
              except: 
                await message.reply("An error occured as I'm unable to execute your command. Discord's character limit is most likely the reason. Try shortening your request.")

client.run(os.getenv("TOKEN"))