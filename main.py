import discord
import datetime
import os

bot_token = os.environ.get("BOT_TOKEN")
guild_id = os.environ.get("GUILD_ID")
log_channel_id = os.environ.get("LOG_CHANNEL_ID")
chat_channel_id = os.environ.get("CHAT_CHANNEL_ID")

client = discord.Client()


@client.event
async def on_ready():
    game = discord.Game("채널 정보를 수집 중")
    await client.change_presence(status=discord.Status.online, activity=game)
    print("READY")

    count = 0
    while count < 5000:
        game = discord.Game(f"메시지 수집 중 / {count}개 삭제")
        await client.change_presence(status=discord.Status.online, activity=game)

        channel = client.get_guild(int(guild_id)).get_channel(int(chat_channel_id))

        after_time = datetime.datetime(2021, 1, 1)
        messages = await channel.history(after=after_time, limit=30).flatten()
        num_of_message = len(messages)

        if num_of_message <= 15:
            break

        for i in messages:
            await i.delete()

            count += 1
            if count % 10 == 0:
                print(f"{count} PROCESSED")
                game = discord.Game(f"{count}개 삭제함!")
                await client.change_presence(status=discord.Status.online, activity=game)

    game = discord.Game(f"작업 마무리 / {count}개 삭제")
    await client.change_presence(status=discord.Status.online, activity=game)

    now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if count != 0:
        channel = client.get_guild(int(guild_id)).get_channel(int(log_channel_id))
        msg = f"{now_time}에 메시지 {count} 개를 삭제하였습니다."
        await channel.send(msg)

    await client.close()

client.run(bot_token)


