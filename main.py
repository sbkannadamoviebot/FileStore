import asyncio
from bot import Bot, web_app
from pyrogram import compose
import config

async def main():
    app = [] # ಇಲ್ಲಿ 4 ಸ್ಪೇಸ್ ಇದೆ
    
    # ಕೆಳಗಿನ ಸಾಲು ಮೇಲಿನ 'app = []' ಗೆ ಸರಿಯಾಗಿ ಸಮನಾಗಿರಬೇಕು
    app.append(
        Bot(
            session=config.SESSION,
            workers=config.WORKERS,
            db=config.DB_CHANNEL,
            fsub=config.FSUBS,
            token=config.BOT_TOKEN,
            admins=config.ADMINS,
            messages=config.MESSAGES,
            auto_del=config.AUTO_DEL,
            db_uri=config.DB_URI,
            db_name=config.DB_NAME,
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            protect=config.PROTECT,
            disable_btn=config.DISABLE_BTN
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

