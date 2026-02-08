import config
import asyncio
from bot import Bot, web_app
from pyrogram import compose
from config import *

async def main():
    app = []

    # Create bot instance using config.py values
    app.append(
               
      Bot(
            # SESSION ಲೈನ್ ತೆಗೆದುಬಿಡು
            WORKERS=config.WORKERS,
            DB_CHANNEL=config.DB_CHANNEL,
            FSUBS=config.FSUBS,
            BOT_TOKEN=config.BOT_TOKEN,
            ADMINS=config.ADMINS,
            # ... ಉಳಿದವು ಹಾಗೆಯೇ ಇರಲಿ

        )

    )

    await compose(app)


async def runner():
    await asyncio.gather(
        main(),
        web_app()
    )

asyncio.run(runner())
