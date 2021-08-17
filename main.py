import discord
from datetime import datetime, timedelta
import os

bot_token = os.environ.get("BOT_TOKEN")
guild_id = os.environ.get("GUILD_ID")
log_channel_id = os.environ.get("LOG_CHANNEL_ID")
chat_channel_id = os.environ.get("CHAT_CHANNEL_ID")

client = discord.Client()


@client.event
async def on_ready():
    count = 0
    await update_status(f"메시지 수집 중 / {count}개 삭제")

    while count < 50000:
        channel = client.get_guild(int(guild_id)).get_channel(int(chat_channel_id))

        after_time = datetime(2021, 1, 1)
        messages = await channel.history(after=after_time, limit=100).flatten()
        num_of_message = len(messages)

        if num_of_message < 100:
            break

        await channel.purge(limit=1)

        count += 1
        print(f"{count} PROCESSED")

        await update_status(f"{count}개 삭제함!")

    await update_status(f"작업 마무리 / {count}개 삭제")

    now_time = (datetime.now() + timedelta(hours=9)).strftime("%Y-%m-%d %H:%M:%S")

    if count != 0:
        channel = client.get_guild(int(guild_id)).get_channel(int(log_channel_id))
        msg = f"{now_time}에 메시지 {count} 개를 삭제하였습니다."
        await channel.send(msg)

    await client.close()


async def update_status(message):
    game = discord.Game(message)
    await client.change_presence(status=discord.Status.online, activity=game)

client.run(bot_token)


