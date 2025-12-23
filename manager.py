from telethon import TelegramClient
import config
import asyncio

async def main():
    print("Welcome to Custom Telegram Toolkit Manager")
    print("----------------------------------------")
    
    client = TelegramClient(config.SESSION_PATH, config.API_ID, config.API_HASH)
    
    print("Connecting to Telegram...")
    await client.connect()
    
    if not await client.is_user_authorized():
        print("Not authorized. Starting login flow...")
        if config.PHONE:
            await client.start(phone=config.PHONE)
        else:
            await client.start()
    
    user = await client.get_me()
    print(f"\nSuccessfully logged in as: {user.first_name} (@{user.username})")
    print(f"Session saved to: {config.SESSION_PATH}.session")
    
    await client.disconnect()

if __name__ == "__main__":
    asyncio.run(main())
