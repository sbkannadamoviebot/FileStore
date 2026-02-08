import asyncio
from bot import Bot, web_app
from pyrogram import compose
import config

async def main():
    app = []
    
    # ನಿನ್ನ bot.py ನಲ್ಲಿರೋ ಹೆಸರುಗಳಿಗೆ (db, fsub, token) ಮ್ಯಾಚ್ ಆಗುವಂತೆ ಇಲ್ಲಿ ಬದಲಾಯಿಸಲಾಗಿದೆ
    app.append(
        Bot(
            session=config.SESSION,
            workers=config.WORKERS,
            db=config.DB_CHANNEL,      # bot.py ಲೈನ್ 17 ರಲ್ಲಿ 'db' ಅಂತ ಇದೆ
            fsub=config.FSUBS,         # bot.py ಲೈನ್ 17 ರಲ್ಲಿ 'fsub' ಅಂತ ಇದೆ
            token=config.BOT_TOKEN,    # bot.py ಲೈನ್ 17 ರಲ್ಲಿ 'token' ಅಂತ ಇದೆ
            admins=config.ADMINS,
            messages=config.MESSAGES,
            auto_del=config.AUTO_DEL,
            db_uri=config.DB_URI,
            db_name=config.DB_NAME,
            api_id=config.API_ID,
            api_hash=config.API_HASH
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

