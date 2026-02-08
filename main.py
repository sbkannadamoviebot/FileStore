from config import BOT_TOKEN
import asyncio
from bot import Bot, web_app
from pyrogram import compose
from config import *

async def main():
    app = []

    # Create bot instance using config.py values
    app.append(
               
    Bot(
            SESSION=config.SESSION,
            WORKERS=config.WORKERS,
            DB_CHANNEL=config.DB_CHANNEL,
            FSUBS=config.FSUBS,
            BOT_TOKEN=config.BOT_TOKEN,
            ADMINS=config.ADMINS,
            MESSAGES=config.MESSAGES,
            AUTO_DEL=config.AUTO_DEL,
            DB_URI=config.DB_URI,
            DB_NAME=config.DB_NAME,
            API_ID=config.API_ID,
            API_HASH=config.API_HASH,
            PROTECT=config.PROTECT,
            DISABLE_BTN=config.DISABLE_BTN
        )

    )

    await compose(app)


async def runner():
    await asyncio.gather(
        main(),
        web_app()
    )

asyncio.run(runner())
