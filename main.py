import discord
import datetime
import os

bot_token = os.environ.get("BOT_TOKEN")
guild_id = os.environ.get("GUILD_ID")
channel_id = os.environ.get("CHANNEL_ID")

client = discord.Client()


@client.event
async def on_ready():
    game = discord.Game("봇 작동 중...")
    await client.change_presence(status=discord.Status.online, activity=game)
    print("READY")

    count = 0
    # while count < 5000:
    channel = client.get_guild(int(guild_id)).get_channel(int(channel_id))

    after_time = datetime.datetime(2021, 1, 1)
    messages = await channel.history(after=after_time, limit=100).flatten()
    num_of_message = len(messages)

    # if num_of_message <= 50:
    #     break

    print(f"{len(messages)} START")
    for i in messages:
        if i.author.id == client.user.id:
            num_of_message -= 1
        else:
            await i.delete()

        count += 1
        if count % 10 == 0:
            print(f"{count}/{len(messages)} PROCESSED")

    now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if count != 0:
        channel = client.get_guild(int(guild_id)).get_channel(int(channel_id))
        msg = f"{now_time}에 메시지 {count} 개를 삭제하였습니다."
        await channel.send(msg)

    await client.close()

client.run(bot_token)


