import asyncio
from telethon import TelegramClient, events
from yandexgptlite import YandexGPTLite

account = YandexGPTLite('b1gck5hl5v4ktgcnlv3m', 'y0_AgAAAABziHH_AATuwQAAAAEMA-UkAACDH9ws6mdEYL9rQubGdlGGpIe4xw' )


api_id = 23966203
api_hash = '85bd96f12b78d9140335ca52ce75120a'

client = TelegramClient('gpt_from_my_tg', api_id, api_hash)



@client.on(events.NewMessage(pattern='/gpt (.+)'))
async def gpt_command(event):
    user_text = event.pattern_match.group(1)  # Получаем текст после команды
    text = account.create_completion(prompt=user_text, temperature='0.6')


    await event.respond(text)

async def main():
    await client.start()
    print('Client started. GO!')

    await client.run_until_disconnected()


asyncio.run(main())

with client:
    client.loop.run_until_complete(main())