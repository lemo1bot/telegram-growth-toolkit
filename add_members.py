import csv
import asyncio
import random
import config
from telethon import TelegramClient, errors, functions
from telethon.tl.types import InputPeerUser, InputPeerChannel

# Configurable delay range (seconds)
# WARNING: FAST MODE (High Ban Risk)
DELAY_MIN = 1
DELAY_MAX = 2

async def add_members_to_group(target_group_link, csv_file='members.csv'):
    client = TelegramClient(config.SESSION_PATH, config.API_ID, config.API_HASH)
    await client.connect()

    if not await client.is_user_authorized():
        return {"status": "error", "message": "Not authorized. Run manager.py first."}

    try:
        target_entity = await client.get_entity(target_group_link)
        print(f"Resolved Target: {target_entity.title}")
    except Exception as e:
        return {"status": "error", "message": f"Error resolving target: {e}"}

    users = []
    try:
        with open(csv_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                users.append(row)
    except FileNotFoundError:
        return {"status": "error", "message": "CSV file not found."}

    print(f"Loaded {len(users)} users from CSV.")
    
    count = 0
    for i, user in enumerate(users):
        try:
            user_to_add = None
            user_id = int(user['User ID'])
            username = user['Username']
            access_hash = int(user['Access Hash'])
            first_name = user['First Name']

            if username:
                user_to_add = await client.get_input_entity(username)
            else:
                user_to_add = InputPeerUser(user_id, access_hash)

            print(f"[{i+1}/{len(users)}] Adding {first_name} ({user_id})...")

            try:
                await client(functions.channels.InviteToChannelRequest(
                    channel=target_entity,
                    users=[user_to_add]
                ))
                print("   Success!")
                count += 1
                if count >= 10:
                    print("TEST LIMIT REACHED: Added 10 users. Stopping.")
                    break
            except errors.PeerFloodError:
                print("CRITICAL: PeerFloodError. Stopping.")
                return {"status": "error", "message": "PeerFloodError: Rate limit hit."}
            except errors.UserPrivacyRestrictedError:
                print("   [SKIP] Privacy: User has 'My Contacts' only. Moving to next...")
            except errors.UserNotMutualContactError:
                print("   [SKIP] Contact: You must be a mutual contact to add. Moving to next...")
            except (errors.UserChannelsTooMuchError, errors.BotGroupsBlockedError) as e:
                print(f"   [SKIP] Other: {type(e).__name__}")
            except Exception as e:
                print(f"   UNEXPECTED ERROR: {type(e).__name__} - {e}")

            delay = random.randint(DELAY_MIN, DELAY_MAX)
            print(f"   Waiting {delay} seconds...")
            await asyncio.sleep(delay)

        except Exception as e:
            print(f"Skipping user resolution error: {e}")

    await client.disconnect()
    return {"status": "success", "count": count}

if __name__ == "__main__":
    target = input("Enter Target Group Link: ")
    asyncio.run(add_members_to_group(target))

