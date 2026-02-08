import asyncio
from bot import Bot, web_app
from pyrogram import compose
import config

async def main():
    app = []
    
    # ಬಾಟ್ ಇನ್ಸ್ಟೆನ್ಸ್ ಕ್ರಿಯೇಟ್ ಮಾಡಲಾಗುತ್ತಿದೆ
    app.append(
        Bot(
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

if __name__ == "__main__":
    asyncio.run(runner())

