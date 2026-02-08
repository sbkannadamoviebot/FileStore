import asyncio
from bot import Bot, web_app
from pyrogram import compose
import config

async def main():
    app = []
    
    # ಬಾಟ್ ಇನ್ಸ್ಟೆನ್ಸ್ ಕ್ರಿಯೇಟ್ ಮಾಡಲಾಗುತ್ತಿದೆ
        app.append(
        Bot(
            session=config.SESSION,
            workers=config.WORKERS,
            db=config.DB_CHANNEL,      # ಇಲ್ಲಿ DB_CHANNEL ಬದಲು db ಅಂತ ಇರಬೇಕು
            fsub=config.FSUBS,         # ಇಲ್ಲಿ FSUBS ಬದಲು fsub ಅಂತ ಇರಬೇಕು
            token=config.BOT_TOKEN,    # ಇಲ್ಲಿ BOT_TOKEN ಬದಲು token ಅಂತ ಇರಬೇಕು
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

