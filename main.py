import asyncio
import os
import random
from typing import Coroutine

import aiohttp
from discord_webhook import AsyncDiscordWebhook, DiscordEmbed
from dotenv import load_dotenv

import data
import generators


async def main() -> Coroutine[any, any, None]:
    person = data.get_person()
    message = generators.generate(person)
    title = f"Nová zpráva {random.choices(['od', 'z'], weights=(4, 1), k=1)[0]} {person}"

    async with aiohttp.client.ClientSession() as session:
        response = await session.head("https://source.unsplash.com/300x300/?pretty-girl", allow_redirects=True)
        image_url = str(response.url)

    webhook = AsyncDiscordWebhook(os.getenv("DISCORD_WEBHOOK"))
    webhook.username = data.get_value("websites")

    embed = DiscordEmbed()
    embed.set_title(title)
    embed.set_thumbnail(url=image_url)
    embed.set_description(message)

    webhook.add_embed(embed)

    await webhook.execute()


if __name__ == "__main__":
    load_dotenv()
    asyncio.run(main())
