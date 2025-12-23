import csv
import asyncio
import random
import config
from telethon import TelegramClient, errors
from telethon.tl.types import InputPeerUser

# Configurable delay range (seconds)
# WARNING: Lowering this increases ban risk significantly.
DELAY_MIN = 30
DELAY_MAX = 60

async def send_mass_messages(message_text, csv_file='members.csv', progress_callback=None):
    if not message_text:
        return {"status": "error", "message": "Message text is empty."}

    client = TelegramClient(config.SESSION_PATH, config.API_ID, config.API_HASH)
    await client.connect()

    if not await client.is_user_authorized():
        return {"status": "error", "message": "Not authorized. Run manager.py first."}

    users = []
    try:
        with open(csv_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                users.append(row)
    except FileNotFoundError:
        return {"status": "error", "message": "CSV file not found."}

    total_users = len(users)
    count = 0
    
    # Notify start
    if progress_callback:
        progress_callback(0, total_users, f"Starting... Found {total_users} users.")

    for i, user in enumerate(users):
        try:
            target = None
            user_id = int(user['User ID'])
            username = user['Username']
            first_name = user['First Name']

            if username:
                target = username
            else:
                try:
                    access_hash = int(user['Access Hash'])
                    target = InputPeerUser(user_id, access_hash)
                except (ValueError, TypeError):
                    continue

            # Send Message
            await client.send_message(target, message_text)
            count += 1
            
            # Progress update
            if progress_callback:
                progress_callback(i+1, total_users, f"Sent to {first_name}")

            # Safe Delay
            delay = random.randint(DELAY_MIN, DELAY_MAX)
            await asyncio.sleep(delay)

        except errors.PeerFloodError:
            return {"status": "error", "message": "PeerFloodError: Telegram says you are spamming. Stopped."}
        except errors.UserPrivacyRestrictedError:
             pass # Skip
        except errors.FloodWaitError as e:
            if e.seconds > 300:
                return {"status": "error", "message": f"FloodWaitError: Need to wait {e.seconds}s. Too long, stopping."}
            await asyncio.sleep(e.seconds)
        except Exception as e:
            pass # Continue on generic error

    await client.disconnect()
    return {"status": "success", "count": count}

if __name__ == "__main__":
    asyncio.run(send_mass_messages())
